# MeshDescriptor

**Framework**: RealityKit  
**Kind**: struct

Defines a 3D mesh’s structure and data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct MeshDescriptor
```

#### Overview

Create or modify 3D shapes in a RealityKit scene using `MeshDescriptor`, which provides properties and methods to define the vertices, normals, texture coordinates, and other attributes of the mesh.

Apply the mesh to an [`Entity`](entity.md) by creating a [`MeshResource`](meshresource.md) with [`generate(from:)`](meshresource/generate(from:)-6l1q2.md), and create a [`ModelComponent`](modelcomponent.md) with [`init(mesh:materials:)`](modelcomponent/init(mesh:materials:).md).

Start by creating a basic triangle with a `MeshDescriptor` instance.

```swift
var descriptor = MeshDescriptor(name: "triangle")
descriptor.positions = MeshBuffers.Positions([
    [-1, -1, 0], [1, -1, 0], [0, 1, 0]
])
descriptor.primitives = .triangles([0, 1, 2])
```

## Topics

### Initializers
- [init(name: String)](meshdescriptor/init(name:).md)
  Creates an empty mesh descriptor.
### Instance Properties
- [var materials: MeshDescriptor.Materials](meshdescriptor/materials-swift.property.md)
  Material assignments.
- [var name: String](meshdescriptor/name.md)
  The name of the mesh.
- [var primitives: MeshDescriptor.Primitives?](meshdescriptor/primitives-swift.property.md)
  The primitives that make up the mesh.
### Enumerations
- [MeshDescriptor.Materials](meshdescriptor/materials-swift.enum.md)
- [MeshDescriptor.Primitives](meshdescriptor/primitives-swift.enum.md)
  Indicates which primitive shape type a mesh applies to its vertex indices.

## Relationships

### Conforms To
- [MeshBufferContainer](meshbuffercontainer.md)

## See Also

- [MeshDescriptor.Primitives](meshdescriptor/primitives-swift.enum.md)
  Indicates which primitive shape type a mesh applies to its vertex indices.
- [MeshDescriptor.Materials](meshdescriptor/materials-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdescriptor)*