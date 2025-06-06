# Choosing Which Camera Feed to Augment

**Framework**: ARKit

Add visual effects to the user’s environment in an AR experience through the front or rear camera.

#### Overview

iOS devices come equipped with multiple cameras, and for each ARKit session you need to choose which camera’s feed to augment. ARKit 3 and later provide simultaneous anchors from all cameras (see [`Combining user face-tracking and world tracking`](combining-user-face-tracking-and-world-tracking.md)), but you still must choose one camera feed to show to the user at a time.

##### Augmented Reality with the Rear Camera

The most common kinds of AR experience display a view from the device’s rear camera, augmented by other visual content, giving the user a new way to see and interact with the world around them.

[`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md) provides this kind of experience: ARKit tracks the real-world the user inhabits, and matches it with a coordinate space for you to place virtual content. World tracking also offers features to make AR experiences more immersive, like the ability to recognize objects and images in the user’s environment and respond to real-world lighting conditions.

##### Augmented Reality with the Front Camera

For iOS devices that have a TrueDepth camera, [`ARFaceTrackingConfiguration`](arfacetrackingconfiguration.md) enables you to augment the front-camera feed, while providing you with real-time tracking for the pose and expression of faces. With that information,  that you might, for example, choose to overlay realistic virtual masks. Or, you might omit the camera view and use facial expression data to animate virtual characters, as in the Animoji app for iMessage.

## See Also

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)
  Keep the user informed on the current session state and recover from interruptions.
- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)
  Control rendering of your app’s virtual content on top of a camera feed.
- [class ARSession](arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- [Configuration Objects](configuration-objects.md)
  Configure your augmented reality session to detect and track specific types of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/choosing-which-camera-feed-to-augment)*