# ARDepthData

**Framework**: ARKit  
**Kind**: class

An object that describes the distance to regions of the real world from the plane of the camera.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ARDepthData
```

#### Overview

This object contains the following depth information that the LiDAR scanner captures at runtime:

- Every pixel in the [`depthMap`](ardepthdata/depthmap.md) maps to a region of the visible scene ([`capturedImage`](arframe/capturedimage.md)), where the pixel value defines that region’s distance from the plane of the camera in meters.
- The [`confidenceMap`](ardepthdata/confidencemap.md) property measures the accuracy of the corresponding depth data in [`depthMap`](ardepthdata/depthmap.md), and is useful in filtering out lower-accuracy depth values if an app’s algorithm required it.

[`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md) exposes this depth information in the [`sceneDepth`](arframe/scenedepth.md) property which it updates every frame. To enable scene depth, add the [`sceneDepth`](arconfiguration/framesemantics-swift.struct/scenedepth.md) frame semantic to a world-tracking configuration’s [`frameSemantics`](arconfiguration/framesemantics-swift.property.md) and frames vended by the session contain [`ARDepthData`](ardepthdata.md) captured by the LiDAR scanner.

## Topics

### Depth Information
- [var depthMap: CVPixelBuffer](ardepthdata/depthmap.md)
  The estimated distance from the device to its environment, in meters.
- [var confidenceMap: CVPixelBuffer?](ardepthdata/confidencemap.md)
  The framework’s confidence in the accuracy of the depth-map data.
- [enum ARConfidenceLevel](arconfidencelevel.md)
  Degrees to which the framework is confident about depth-data accuracy.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Displaying a point cloud using scene depth](displaying-a-point-cloud-using-scene-depth.md)
  Present a visualization of the physical environment by placing points based a scene’s depth data.
- [Creating a fog effect using scene depth](creating-a-fog-effect-using-scene-depth.md)
  Apply virtual fog to the physical environment.
- [class ARFrame](arframe.md)
  A video image captured as part of a session with position-tracking information.
- [class ARPointCloud](arpointcloud.md)
  A collection of points in the world coordinate space of the AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ardepthdata)*