# ARSCNFaceGeometry

**Framework**: ARKit  
**Kind**: class

A SceneKit representation of face topology for use with face information that an AR session provides.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARSCNFaceGeometry
```

#### Overview

This class is a subclass of [`SCNGeometry`](https://developer.apple.com/documentation/SceneKit/SCNGeometry) that wraps the mesh data provided by the [`ARFaceGeometry`](arfacegeometry.md) class. You can use [`ARSCNFaceGeometry`](arscnfacegeometry.md) to quickly and easily visualize face topology and facial expressions provided by ARKit in a SceneKit view.

> ❗ **Important**:  [`ARSCNFaceGeometry`](arscnfacegeometry.md) is available only in SceneKit views or renderers that use Metal. This class is not supported for OpenGL-based SceneKit rendering.

 [`ARSCNFaceGeometry`](arscnfacegeometry.md) is available only in SceneKit views or renderers that use Metal. This class is not supported for OpenGL-based SceneKit rendering.

Face mesh topology is constant for the lifetime of an [`ARSCNFaceGeometry`](arscnfacegeometry.md) object. That is, the geometry’s single [`SCNGeometryElement`](https://developer.apple.com/documentation/SceneKit/SCNGeometryElement) object always describes the same arrangement of vertices, and the [`texcoord`](https://developer.apple.com/documentation/SceneKit/SCNGeometrySource/Semantic-swift.struct/texcoord) geometry source always maps the same vertices to the same texture coordinates.

When you modify the geometry with the [`update(from:)`](arscnfacegeometry/update(from:).md) method, only the contents of the [`vertex`](https://developer.apple.com/documentation/SceneKit/SCNGeometrySource/Semantic-swift.struct/vertex) geometry source change, indicating the difference in vertex positions as ARKit adapts the mesh to the shape and expression of the user’s face.

## Topics

### Creating a Geometry
- [convenience init?(device: any MTLDevice)](arscnfacegeometry/init(device:).md)
  Creates a SceneKit face geometry for rendering with the specified Metal device object.
- [convenience init?(device: any MTLDevice, fillMesh: Bool)](arscnfacegeometry/init(device:fillmesh:).md)
  Creates a SceneKit face geometry, optionally filling in gaps in the mesh for the eyes and mouth.
### Updating the Geometry
- [func update(from: ARFaceGeometry)](arscnfacegeometry/update(from:).md)
  Deforms the SceneKit geometry to match the specified face mesh.

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

- [Tracking and visualizing faces](tracking-and-visualizing-faces.md)
  Detect faces in a front-camera AR experience, overlay virtual content, and animate facial expressions in real-time.
- [Combining user face-tracking and world tracking](combining-user-face-tracking-and-world-tracking.md)
  Track the user’s face in an app that displays an AR experience with the rear camera.
- [class ARFaceGeometry](arfacegeometry.md)
  A 3D mesh describing face topology for use in face-tracking AR sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnfacegeometry)*