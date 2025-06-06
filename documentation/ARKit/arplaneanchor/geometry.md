# geometry

**Framework**: ARKit  
**Kind**: property

A coarse triangle mesh representing the general shape of the detected plane.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
var geometry: ARPlaneGeometry { get }
```

#### Discussion

This mesh provides vertex, index, and texture coordinate buffers describing the estimated 2D footprint of the plane.

You can visualize the plane geometry by passing these buffers to your preferred rendering engine. To visualize a plane geometry using SceneKit, create an [`ARSCNPlaneGeometry`](arscnplanegeometry.md) instance and use its [`update(from:)`](arscnplanegeometry/update(from:).md) method to update it to match the plane geometry.

## See Also

- [class ARPlaneGeometry](arplanegeometry.md)
  A 3D mesh describing the shape of a detected plane in world-tracking AR sessions.
- [class ARSCNPlaneGeometry](arscnplanegeometry.md)
  A SceneKit representation of the 2D shape of a plane, for use with plane detection results in an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/geometry)*