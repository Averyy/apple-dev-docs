# Configuration Objects

**Framework**: ARKit

Configure your augmented reality session to detect and track specific types of content.

#### Overview

Configuration objects define how ARKit sets up and runs your augmented reality session. Although [`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md) provides the widest range of features in a rear-camera experience, each feature consumes device energy and compute cycles. So to maximize device uptime and performance, enable additional options sparingly.

If another AR configuration fulfills your requirements with a more concise feature set, use that configuration instead. For example, use [`ARBodyTrackingConfiguration`](arbodytrackingconfiguration.md) instead of a world-tracking configuration for 3D motion-capture if you don’t need user face-tracking, collaboration, or scene reconstruction.

##### Select Frame Features

Some configurations support subfeatures that relate to a session’s frame. Enable these features by setting the following flags in the configuration’s [`frameSemantics`](arconfiguration/framesemantics-swift.property.md):

Use [`supportsFrameSemantics(_:)`](arconfiguration/supportsframesemantics(_:).md) to verify whether the iOS device supports the [`ARConfiguration.FrameSemantics`](arconfiguration/framesemantics-swift.struct.md) you desire before setting [`frameSemantics`](arconfiguration/framesemantics-swift.property.md).

> ❗ **Important**:  To maximize device responsiveness, refrain from turning on people occlusion for single-user experiences when you don’t expect people in the scene.

 To maximize device responsiveness, refrain from turning on people occlusion for single-user experiences when you don’t expect people in the scene.

##### Switch Configurations at Runtime

To toggle features like plane detection, frame semantics, and environment texturing, you switch your configuration at runtime by calling [`runWithConfiguration:`](arsession/runwithconfiguration:.md) on your existing session. Where possible, ARKit maintains all the information collected during the session under the prior configuration, such as information about the physical environment and anchors.

> 💡 **Tip**:  You can gracefully downgrade the AR experience in the event of low-power or thermal events. For example, you could temporarily switch from a world-tracking configuration to a position-tracking configuration ([`ARPositionalTrackingConfiguration`](arpositionaltrackingconfiguration.md)) if your app can function at a basic level in that limited capacity until the device cools down.

 You can gracefully downgrade the AR experience in the event of low-power or thermal events. For example, you could temporarily switch from a world-tracking configuration to a position-tracking configuration ([`ARPositionalTrackingConfiguration`](arpositionaltrackingconfiguration.md)) if your app can function at a basic level in that limited capacity until the device cools down.

If your session switches between face- and world-tracking configurations, the session doesn’t maintain state.

##### Enable High Quality Video and Custom Capture Settings

In iOS 16, you can enable a 4K and high dynamic range (HDR) video format. In addition, you can customize your session’s video settings through the underlying AV capture device.

To determine whether your session supports 4K, call [`recommendedVideoFormatFor4KResolution`](arconfiguration/recommendedvideoformatfor4kresolution.md).

```swift
guard let hiResFormat = ARWorldTrackingConfiguration.recommendedVideoFormatFor4KResolution else {
   print("4K video format not supported."); return }
```

Then, create a configuration with the format. You can also indicate the intent to enable HDR by setting [`videoHDRAllowed`](arconfiguration/videohdrallowed.md) to `true`.

```swift
var config = ARWorldTrackingConfiguration()
config.videoFormat = hiResFormat
config.videoHDRAllowed = true
session.run(config)
```

If the device supports a configurable capture session, the [`configurableCaptureDeviceForPrimaryCamera`](arconfiguration/configurablecapturedeviceforprimarycamera.md) provides the underlying capture device that you can adjust as needed.

```swift
if let device = ARWorldTrackingConfiguration.configurableCaptureDeviceForPrimaryCamera {
   do { try device.lockForConfiguration()
      // Configure capture settings here.
      device.unlockForConfiguration()
   } catch { /* Error handling. */ }
}
```

##### Capture High Resolution Still Frames

In iOS 16, you can enable high-resolution frame capture by calling [`recommendedVideoFormatForHighResolutionFrameCapturing`](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md) on your configuration. If the device supports high-resolution stills, the function returns a video format you can use to start a session:

```swift
guard let hiResFormat = type(of: config).recommendedVideoFormatForHighResolutionFrameCapturing else {
    fatalError("The device doesn't support high-resolution stills.") }
config.videoFormat = hiResFormat
arSession.run(config)
```

During the session, capture a high-resolution still frame at any time by calling [`captureHighResolutionFrame(completion:)`](arsession/capturehighresolutionframe(completion:).md):

```swift
arSession.captureHighResolutionFrame { (frame, error) in
    if let frame = frame {
        saveHiResFrame(frame)
    } else { /* Error handling. */ }
```

## Topics

### Common Configuration Details
- [class ARConfiguration](arconfiguration.md)
  The base object that contains information about how to configure an augmented reality session.
### Spatial Tracking
- [Understanding World Tracking](understanding-world-tracking.md)
  Discover features and best practices for building rear-camera AR experiences.
- [class ARWorldTrackingConfiguration](arworldtrackingconfiguration.md)
  A configuration that tracks the position of a device in relation to objects in the environment.
- [class ARGeoTrackingConfiguration](argeotrackingconfiguration.md)
  A configuration that tracks locations with GPS, map data, and a device’s compass.
- [class AROrientationTrackingConfiguration](arorientationtrackingconfiguration.md)
  A configuration that tracks only the device’s orientation using the rear-facing camera.
- [class ARPositionalTrackingConfiguration](arpositionaltrackingconfiguration.md)
  A configuration that tracks only the device’s position in 3D space.
### Body and Face Tracking
- [class ARBodyTrackingConfiguration](arbodytrackingconfiguration.md)
  A configuration that tracks human body poses, planar surfaces, and images using the rear-facing camera.
- [class ARFaceTrackingConfiguration](arfacetrackingconfiguration.md)
  A configuration that tracks facial movement and expressions using the front camera.
### Image Recognition
- [class ARImageTrackingConfiguration](arimagetrackingconfiguration.md)
  A configuration that tracks known images using the rear-facing camera.
### Object Detection
- [class ARObjectScanningConfiguration](arobjectscanningconfiguration.md)
  A configuration that recognizes objects and collects high-fidelity data about specific objects using the rear-facing camera.

## See Also

- [Choosing Which Camera Feed to Augment](choosing-which-camera-feed-to-augment.md)
  Add visual effects to the user’s environment in an AR experience through the front or rear camera.
- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)
  Keep the user informed on the current session state and recover from interruptions.
- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)
  Control rendering of your app’s virtual content on top of a camera feed.
- [class ARSession](arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/configuration-objects)*