# ARFrame

**Framework**: ARKit  
**Kind**: class

A video image captured as part of a session with position-tracking information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARFrame
```

## Mentions

- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)

#### Overview

A running session continuously captures video frames from the device’s camera while ARKit analyzes the captures to determine the user’s position in the world. ARKit can provide this information to you in the form of an [`ARFrame`](arframe.md) in two ways:

- Occasionally, by accessing an [`ARSession`](arsession.md) object’s [`currentFrame`](arsession/currentframe.md)
- Constantly, as a stream of frames through the [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-9v2kw.md) callback

To automatically receive all frames as ARKit captures them, make one of your objects the [`delegate`](arsession/delegate.md) of your app’s [`ARSession`](arsession.md).

Each frame can contain additional data, for example, EXIF ([`exifData`](arframe/exifdata.md)), or data based on any particular [`frameSemantics`](arconfiguration/framesemantics-swift.property.md) that you enable.

## Topics

### Accessing camera data
- [var camera: ARCamera](arframe/camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var capturedImage: CVPixelBuffer](arframe/capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var timestamp: TimeInterval](arframe/timestamp.md)
  The time at which the frame was captured.
- [var cameraGrainIntensity: Float](arframe/cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var cameraGrainTexture: (any MTLTexture)?](arframe/cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.
- [var exifData: [String : Any]](arframe/exifdata.md)
  Auxiliary data for the captured image.
### Accessing scene data
- [var lightEstimate: ARLightEstimate?](arframe/lightestimate.md)
  An estimate of lighting conditions based on the camera image.
- [func displayTransform(for: UIInterfaceOrientation, viewportSize: CGSize) -> CGAffineTransform](arframe/displaytransform(for:viewportsize:).md)
  Returns an affine transform for converting between normalized image coordinates and a coordinate space appropriate for rendering the camera image onscreen.
- [var rawFeaturePoints: ARPointCloud?](arframe/rawfeaturepoints.md)
  The current intermediate results of the scene analysis ARKit uses to perform world tracking.
- [var capturedDepthData: AVDepthData?](arframe/captureddepthdata.md)
  Depth data captured in front-camera experiences.
- [var capturedDepthDataTimestamp: TimeInterval](arframe/captureddepthdatatimestamp.md)
  The time at which depth data for the frame (if any) was captured.
- [var sceneDepth: ARDepthData?](arframe/scenedepth.md)
  Data on the distance between a device’s rear camera and real-world objects in an AR experience.
- [var smoothedSceneDepth: ARDepthData?](arframe/smoothedscenedepth.md)
  An average of distance measurements between a device’s rear camera and real-world objects that creates smoother visuals in an AR experience.
### Tracking and interacting with the real world
- [var anchors: [ARAnchor]](arframe/anchors.md)
  The list of anchors representing positions tracked or objects detected in the scene.
- [func raycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery](arframe/raycastquery(from:allowing:alignment:).md)
  Get a ray-cast query for a screen point.
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arframe/hittest(_:types:).md)
  Searches for real-world objects or AR anchors in the captured camera image.
### Checking world-mapping status
- [var worldMappingStatus: ARFrame.WorldMappingStatus](arframe/worldmappingstatus-swift.property.md)
  The feasibility of generating or relocalizing a world map for this frame.
- [ARFrame.WorldMappingStatus](arframe/worldmappingstatus-swift.enum.md)
  A value describing the world mapping status for the area visible in a given frame.
### Checking for people
- [var detectedBody: ARBody2D?](arframe/detectedbody.md)
  The screen position information of a body that ARKit recognizes in the camera image.
- [class ARBody2D](arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [var segmentationBuffer: CVPixelBuffer?](arframe/segmentationbuffer.md)
  A buffer that contains pixel information identifying the shape of objects from the camera feed that you use to occlude virtual content.
- [var estimatedDepthData: CVPixelBuffer?](arframe/estimateddepthdata.md)
  A buffer that represents the estimated depth values from the camera feed that you use to occlude virtual content.
- [ARFrame.SegmentationClass](arframe/segmentationclass.md)
  A categorization of a pixel that defines a type of content you use to occlude your app’s virtual content.
### Assessing geo-tracking condition
- [var geoTrackingStatus: ARGeoTrackingStatus?](arframe/geotrackingstatus.md)
  The session’s condition with respect to geographic tracking at the time the session captured the frame.
- [class ARGeoTrackingStatus](argeotrackingstatus.md)
  The state, accuracy, and reason that are possible for geo-tracking’s current condition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var currentFrame: ARFrame?](arsession/currentframe.md)
  The most recent still frame captured by the active camera feed, including ARKit’s interpretation of it.
- [func captureHighResolutionFrame(completion: (ARFrame?, (any Error)?) -> Void)](arsession/capturehighresolutionframe(completion:).md)
  Requests a frame outside of the normal frequency that contains a high-resolution captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe)*