# ARSCNFaceGeometry

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

A SceneKit representation of face topology for use with face information that an AR session provides.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
class ARSCNFaceGeometry
```

```objc
@interface ARSCNFaceGeometry : SCNGeometry
```

## Overview

This class is a subclass of [`SCNGeometry`](../SceneKit/scngeometry.md) that wraps the mesh data provided by the [`ARFaceGeometry`](./arfacegeometry.md) class. You can use [`ARSCNFaceGeometry`](./arscnfacegeometry.md) to quickly and easily visualize face topology and facial expressions provided by ARKit in a SceneKit view.

> ❗ **Important**:  [`ARSCNFaceGeometry`](./arscnfacegeometry.md) is available only in SceneKit views or renderers that use Metal. This class is not supported for OpenGL-based SceneKit rendering.

Face mesh topology is constant for the lifetime of an [`ARSCNFaceGeometry`](./arscnfacegeometry.md) object. That is, the geometry’s single [`SCNGeometryElement`](../SceneKit/scngeometryelement.md) object always describes the same arrangement of vertices, and the [`texcoord`](../SceneKit/scngeometrysource/semantic-swift.struct/texcoord.md) geometry source always maps the same vertices to the same texture coordinates.

When you modify the geometry with the [`update(from:)`](./arscnfacegeometry/update%28from%29.md) method, only the contents of the [`vertex`](../SceneKit/scngeometrysource/semantic-swift.struct/vertex.md) geometry source change, indicating the difference in vertex positions as ARKit adapts the mesh to the shape and expression of the user’s face.

## Topics

### Creating a Geometry
- [convenience init?(device: any MTLDevice)](./arscnfacegeometry/init%28device%29.md)
  Creates a SceneKit face geometry for rendering with the specified Metal device object.
- [convenience init?(device: any MTLDevice, fillMesh: Bool)](./arscnfacegeometry/init%28device,fillmesh%29.md)
  Creates a SceneKit face geometry, optionally filling in gaps in the mesh for the eyes and mouth.
### Updating the Geometry
- [func update(from: ARFaceGeometry)](./arscnfacegeometry/update%28from%29.md)
  Deforms the SceneKit geometry to match the specified face mesh.
### Initializers
- [convenience init()](./arscnfacegeometry/init%28%29.md)

## Relationships

### Inherits From
- [SCNGeometry](../SceneKit/scngeometry.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [SCNAnimatable](../SceneKit/scnanimatable.md)
- [SCNBoundingVolume](../SceneKit/scnboundingvolume.md)
- [SCNShadable](../SceneKit/scnshadable.md)

## See Also

### Face Data
- [Tracking and visualizing faces](./tracking-and-visualizing-faces.md)
  Detect faces in a front-camera AR experience, overlay virtual content, and animate facial expressions in real-time.
- [Combining user face-tracking and world tracking](./combining-user-face-tracking-and-world-tracking.md)
  Track the user’s face in an app that displays an AR experience with the rear camera.
- [class ARFaceGeometry](./arfacegeometry.md)
  A 3D mesh describing face topology for use in face-tracking AR sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnfacegeometry)*