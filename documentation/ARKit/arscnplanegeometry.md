# ARSCNPlaneGeometry

**Framework**: ARKit  
**Kind**: class

A SceneKit representation of the 2D shape of a plane, for use with plane detection results in an AR session.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
class ARSCNPlaneGeometry
```

#### Overview

[`ARSCNPlaneGeometry`](arscnplanegeometry.md) is a subclass of [`SCNGeometry`](https://developer.apple.com/documentation/scenekit/scngeometry) that wraps the mesh data provided by the [`ARPlaneGeometry`](arplanegeometry.md) class. You can use [`ARSCNPlaneGeometry`](arscnplanegeometry.md) to visualize the plane shape estimates provided by ARKit in a SceneKit view.

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
- [SCNGeometry](../scenekit/scngeometry.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [SCNAnimatable](../scenekit/scnanimatable.md)
- [SCNBoundingVolume](../scenekit/scnboundingvolume.md)
- [SCNShadable](../scenekit/scnshadable.md)

## See Also

- [var geometry: ARPlaneGeometry](arplaneanchor/geometry.md)
  A coarse triangle mesh representing the general shape of the detected plane.
- [class ARPlaneGeometry](arplanegeometry.md)
  A 3D mesh describing the shape of a detected plane in world-tracking AR sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnplanegeometry)*