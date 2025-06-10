# Managing Session Life Cycle and Tracking Quality

**Framework**: ARKit

Keep the user informed on the current session state and recover from interruptions.

#### Overview

World-tracking AR sessions use a technique called  This process combines motion sensor data with computer vision analysis of camera imagery to track the device’s position and orientation in real-world space, also known as , which is expressed in the [`ARCamera`](arcamera.md) [`transform`](arcamera/transform.md) property. For best results, world tracking needs consistent sensor data and camera imagery with visual complexity or recognizable features.

When you start a session, it takes some time for ARKit to gather enough data to precisely model device pose. During a session, the conditions that affect world-tracking quality can change. Use [`ARSessionObserver`](arsessionobserver.md) delegate methods and [`ARCamera`](arcamera.md) properties to follow these changes.

##### Basic Lifecycle of an Ar Session

The figure below shows the changes in tracking state when you start running an AR session.

![Sequence diagram with ARKit tracking state proceeding from notAvailable to limited (initializing) to normal.](https://docs-assets.developer.apple.com/published/6c1b298c9841423519925b31f7548a52/media-3000192%402x.png)

Immediately after you run a new session, the tracking state for provided frames is [`ARCamera.TrackingState.notAvailable`](arcamera/trackingstate-swift.enum/notavailable.md), indicating that ARKit has not yet gathered enough information to estimate the device’s pose.

A few frames later, the tracking state changes to [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md), indicating that a device pose is available but its accuracy is uncertain. A limited state always includes a reason for reduced tracking quality; in this case, the session is still [`ARCamera.TrackingState.Reason.initializing`](arcamera/trackingstate-swift.enum/reason/initializing.md).

After a short time, the tracking state changes to [`ARCamera.TrackingState.normal`](arcamera/trackingstate-swift.enum/normal.md), indicating that the device pose is accurate and all ARKit features are available.

##### Provide Feedback for Tracking Quality Changes

The figure below shows changes in tracking state that can occur due to user interaction or changes in the environment.

![Sequence diagram with ARKit tracking state proceeding from normal to limited (insufficient features) and back to normal.](https://docs-assets.developer.apple.com/published/820df2638e0ca6eeb97b5b72d7afd9d8/media-3000193%402x.png)

When tracking quality is [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md), features that depend on ARKit mapping the user’s local environment are not available:

- Plane detection does not add or update plane anchors
- Hit-testing methods provide no results

A session can enter a [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md) tracking state at any time, based on changes in the user’s local environment or the user moving the device. For example, if the user points the device at a blank wall, or the lights in the room go out, tracking quality may be reduced due to [`ARCamera.TrackingState.Reason.insufficientFeatures`](arcamera/trackingstate-swift.enum/reason/insufficientfeatures.md).

Use the associated [`ARCamera.TrackingState.Reason`](arcamera/trackingstate-swift.enum/reason.md) value to provide feedback that guides the user to resolving the situation so that the tracking state can return to [`ARCamera.TrackingState.normal`](arcamera/trackingstate-swift.enum/normal.md).

##### Recover From Session Interruptions

ARKit can’t track device pose without a running [`ARSession`](arsession.md). By default, if your session is interrupted (for example, by switching to another app), any virtual content in that session is likely out of place relative to the real-world environment.

You can use  to try to recover from an interruption. If you return true from the [`sessionShouldAttemptRelocalization(_:)`](arsessionobserver/sessionshouldattemptrelocalization(_:).md) method, ARKit attempts to reconcile its knowledge of the user’s environment from before the interruption with current camera and sensor data. During this process, the tracking state is [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md) (with [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md) as the reason). If successful, the tracking state returns to [`ARCamera.TrackingState.normal`](arcamera/trackingstate-swift.enum/normal.md) after a short time.

![Sequence diagram with normal tracking state before the session is interrupted, then, after the interruption, proceeding from notAvailable to limited (initializing) to limited (relocalizing) to normal.](https://docs-assets.developer.apple.com/published/dcbfef6d91d046466a2b2384cb41efd7/media-3000194%402x.png)

For relocalization to succeed, the device must be returned to a position and orientation near where it was when the session was interrupted. If these conditions never occur (for example, if the device has moved to an entirely different environment), the session remains in the [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md) state indefinitely.

> ❗ **Important**:  When your app is in the [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md) state, offer the user a way to reset the session (with [`run(_:options:)`](arsession/run(_:options:).md) and [`resetTracking`](arsession/runoptions/resettracking.md)) in case relocalization never succeeds.

##### Create a Persistent Ar Experience

In iOS 12.0 and later, the [`ARWorldMap`](arworldmap.md) class stores the information that ARKit uses to resume a session. By saving a world map to a file, you can use the same relocalization process either to recover from a brief interruption or to resume from an earlier session, even if your app has relaunched. World maps include anchors, so you can also replace virtual content to match an earlier session.

> ❗ **Important**:  The reliability of using [`ARWorldMap`](arworldmap.md) to resume a session strongly depends on the real-world environment. For example, it’s easy to successfully relocalize to a map recorded indoors under consistent artificial lighting, or to a map captured only moments beforehand. Success is less likely when lighting conditions or features of the local environment have changed over time.

![Sequence diagram with normal tracking state, saving a world map before the app closes. Upon relaunching the app and loading the saved map, tracking state proceeds from notAvailable to limited (initializing) to limited (relocalizing).](https://docs-assets.developer.apple.com/published/d8356d1f883f97d38a6730faad22413b/media-3000195%402x.png)

To allow the user to come back to the same AR session after leaving your app, you might save the world map explicitly upon a user action, or automatically in [`applicationDidEnterBackground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidEnterBackground(_:)). Save the world map only if your AR session has state worth saving—for example, if the user has placed virtual objects whose positions you want to remember, and the session is in the [`ARFrame.WorldMappingStatus.mapped`](arframe/worldmappingstatus-swift.enum/mapped.md) state (or has been in that state at least once during the session).

To relocalize to a saved world map, use the [`initialWorldMap`](arworldtrackingconfiguration/initialworldmap.md) property when running a session. Like when resuming from an interruption, the session starts in the [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md) ([`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md)) tracking state. If ARKit can reconcile the world map with the current environment, the tracking state becomes [`ARCamera.TrackingState.normal`](arcamera/trackingstate-swift.enum/normal.md) after a short time, indicating that the session matches the recorded world map.

> 💡 **Tip**:  For relocalization to succeed, the device needs to visit areas of the local environment that it passed through before creating the map—you might assist the user with this task by saving a screenshot with the world map and displaying it as a placement guide when attempting to relocalize.

A session resumed from a world map includes all anchors saved in that world map. If you use the [`name`](aranchor/name.md) property to identify virtual objects you’ve placed anchors for, you can refer to the anchors in the resumed session to recreate that virtual content. To ensure that such content is placed correctly, display it only after the session’s tracking state changes to [`ARCamera.TrackingState.normal`](arcamera/trackingstate-swift.enum/normal.md).

If ARKit cannot reconcile the recorded world map with the current environment (for example, if the device is in an entirely different place from where the world map was recorded), the session remains in the [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md) state indefinitely. Provide users with a way to restart the session in case they can’t resume it. To give up on world map relocalization, call [`run(_:options:)`](arsession/run(_:options:).md) on the session again, with the [`resetTracking`](arsession/runoptions/resettracking.md) option and a configuration whose [`initialWorldMap`](arworldtrackingconfiguration/initialworldmap.md) is `nil`.

## See Also

- [Choosing Which Camera Feed to Augment](choosing-which-camera-feed-to-augment.md)
  Add visual effects to the user’s environment in an AR experience through the front or rear camera.
- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)
  Control rendering of your app’s virtual content on top of a camera feed.
- [class ARSession](arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- [Configuration Objects](configuration-objects.md)
  Configure your augmented reality session to detect and track specific types of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/managing-session-life-cycle-and-tracking-quality)*