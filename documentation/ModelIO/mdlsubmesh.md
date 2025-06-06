# MDLSubmesh

**Framework**: Model I/O  
**Kind**: class

A container for index buffer data and material information to be used in rendering all or part of a 3D object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLSubmesh
```

#### Overview

Submeshes are contained in [`MDLMesh`](mdlmesh.md) objects, which provide vertex buffer data that a submesh’s index data refers to. Together, the vertex and index data describe the geometric form of a portion of the mesh, and the submesh’s [`material`](mdlsubmesh/material.md) property determines its intended surface appearance for rendering.

## Topics

### Creating a Submesh
- [init(indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)](mdlsubmesh/init(indexbuffer:indexcount:indextype:geometrytype:material:).md)
  Initializes a submesh with an index buffer and the specified properties.
- [init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:).md)
  Initializes a named submesh with an index buffer and the specified properties.
- [init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?, topology: MDLSubmeshTopology?)](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:topology:).md)
  Initializes a named submesh with a specific topology.
- [init?(mdlSubmesh: MDLSubmesh, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType)](mdlsubmesh/init(mdlsubmesh:indextype:geometrytype:).md)
  Initializes a submesh by copying or converting another submesh.
### Working with a Submesh’s Index Buffer
- [var indexBuffer: any MDLMeshBuffer](mdlsubmesh/indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexCount: Int](mdlsubmesh/indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](mdlsubmesh/indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](mdlsubmesh/geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](mdlsubmesh/topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](mdlsubmesh/indexbuffer(asindextype:).md)
### Associating Materials with a Submesh
- [var material: MDLMaterial?](mdlsubmesh/material.md)
  An object that describes the intended surface appearance of the submesh for rendering.
### Identifying a Submesh
- [var name: String](mdlsubmesh/name.md)
  A descriptive name for the submesh.
### Constants
- [enum MDLIndexBitDepth](mdlindexbitdepth.md)
  Options for the size of integer data in a submesh’s index buffer, used by the [`indexType`](mdlsubmesh/indextype.md) property.
- [enum MDLGeometryType](mdlgeometrytype.md)
  Types of geometric primitives for rendering a submesh, used by the [`geometryType`](mdlsubmesh/geometrytype.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLAsset](mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLObject](mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLTransform](mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLMesh](mdlmesh.md)
  A container for vertex buffer data to be used in rendering a 3D object.
- [class MDLSubmeshTopology](mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.
- [protocol MDLNamed](mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh)*