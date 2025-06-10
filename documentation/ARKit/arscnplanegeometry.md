# ARSCNPlaneGeometry

**Framework**: ARKit  
**Kind**: class

A SceneKit representation of the 2D shape of a plane, for use with plane detection results in an AR session.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARSCNPlaneGeometry
```

#### Overview

[`ARSCNPlaneGeometry`](arscnplanegeometry.md) is a subclass of [`SCNGeometry`](https://developer.apple.com/documentation/SceneKit/SCNGeometry) that wraps the mesh data provided by the [`ARPlaneGeometry`](arplanegeometry.md) class. You can use [`ARSCNPlaneGeometry`](arscnplanegeometry.md) to visualize the plane shape estimates provided by ARKit in a SceneKit view.

> ❗ **Important**:  [`ARSCNPlaneGeometry`](arscnplanegeometry.md) is available only in SceneKit views or renderers that use Metal. This class is not supported for OpenGL-based SceneKit rendering.

As your AR session continues to run, ARKit provides refined estimates of a detected plane’s 2D shape. Use the [`update(from:)`](arscnplanegeometry/update(from:).md) method to incorporate those refinements into the plane’s SceneKit representation.

## Topics

### Creating a Geometry
- [convenience init?(device: any MTLDevice)](arscnplanegeometry/init(device:).md)
  Creates a SceneKit plane geometry for rendering with the specified Metal device object.
### Updating the Geometry
- [func update(from: ARPlaneGeometry)](arscnplanegeometry/update(from:).md)
  Reshapes the SceneKit geometry to match the specified plane mesh.

## Relationships

### Inherits From
- [SCNGeometry](../SceneKit/SCNGeometry.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](../SceneKit/SCNAnimatable.md)
- [SCNBoundingVolume](../SceneKit/SCNBoundingVolume.md)
- [SCNShadable](../SceneKit/SCNShadable.md)

## See Also

- [var geometry: ARPlaneGeometry](arplaneanchor/geometry.md)
  A coarse triangle mesh representing the general shape of the detected plane.
- [class ARPlaneGeometry](arplanegeometry.md)
  A 3D mesh describing the shape of a detected plane in world-tracking AR sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnplanegeometry)*