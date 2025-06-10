# ARPointCloud

**Framework**: ARKit  
**Kind**: class

A collection of points in the world coordinate space of the AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARPointCloud
```

#### Overview

Use the [`ARFrame`](arframe.md) [`rawFeaturePoints`](arframe/rawfeaturepoints.md) property to obtain a point cloud representing intermediate results of the scene analysis ARKit uses to perform world tracking.

## Topics

### Identifying Feature Points
- [var points: [simd_float3]](arpointcloud/points-4vkif.md)
  The list of detected points.
- [var identifiers: [UInt64]](arpointcloud/identifiers-508tf.md)
  A list of unique identifiers corresponding to detected feature points.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Displaying a point cloud using scene depth](displaying-a-point-cloud-using-scene-depth.md)
  Present a visualization of the physical environment by placing points based a scene’s depth data.
- [Creating a fog effect using scene depth](creating-a-fog-effect-using-scene-depth.md)
  Apply virtual fog to the physical environment.
- [class ARFrame](arframe.md)
  A video image captured as part of a session with position-tracking information.
- [class ARDepthData](ardepthdata.md)
  An object that describes the distance to regions of the real world from the plane of the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arpointcloud)*