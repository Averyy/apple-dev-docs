# ARPlaneGeometry

**Framework**: ARKit  
**Kind**: class

A 3D mesh describing the shape of a detected plane in world-tracking AR sessions.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARPlaneGeometry
```

#### Overview

This class provides the estimated general shape of a detected plane, in the form of a detailed 3D mesh appropriate for use with various rendering technologies or for exporting 3D assets. (For a quick way to visualize a plane geometry using SceneKit, see the [`ARSCNPlaneGeometry`](arscnplanegeometry.md) class.)

Unlike the [`ARPlaneAnchor`](arplaneanchor.md) [`center`](arplaneanchor/center.md) and [`extent`](arplaneanchor/extent.md) properties, which estimate only a rectangular area for a detected plane, a plane anchor’s [`geometry`](arplaneanchor/geometry.md) property provides a more detailed estimate of  the 2D area covered by that plane. For example, if ARKit detects a circular tabletop, the resulting [`ARPlaneGeometry`](arplanegeometry.md) objects roughly match the general shape of the table. As the session continues to run, ARKit provides updated plane anchors whose associated geometry refines the estimated shape of the plane.

You can use this model to more precisely place 3D content that should appear only on a detected flat surface. For example, to ensure that virtual objects don’t fall off the edge of a table. You can also use this model to create occlusion geometry, which hides other virtual content behind the detected surface in the camera image.

The shape of a plane geometry is always convex. That is, the boundary polygon for a plane geometry is a minimal convex hull enclosing all points that ARKit recognizes or estimates are part of the plane.

## Topics

### Accessing Mesh Data
- [var vertices: [simd_float3]](arplanegeometry/vertices-43kle.md)
  An array of vertex positions for each point in the plane mesh.
- [var textureCoordinates: [vector_float2]](arplanegeometry/texturecoordinates-p801.md)
  An array of texture coordinate values for each point in the plane mesh.
- [var triangleCount: Int](arplanegeometry/trianglecount.md)
  The number of triangles described by the [`triangleIndices`](arplanegeometry/triangleindices-1azi3.md) buffer.
- [var triangleIndices: [Int16]](arplanegeometry/triangleindices-64epx.md)
  An array of indices describing the triangle mesh formed by the plane geometry’s vertex data.
### Finding Boundary Points
- [var boundaryVertices: [simd_float3]](arplanegeometry/boundaryvertices-3h98l.md)
  An array of vertex positions for each point along the plane’s boundary.

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

- [var geometry: ARPlaneGeometry](arplaneanchor/geometry.md)
  A coarse triangle mesh representing the general shape of the detected plane.
- [class ARSCNPlaneGeometry](arscnplanegeometry.md)
  A SceneKit representation of the 2D shape of a plane, for use with plane detection results in an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry)*