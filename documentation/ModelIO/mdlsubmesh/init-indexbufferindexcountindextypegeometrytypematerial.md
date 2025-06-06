# init(indexBuffer:indexCount:indexType:geometryType:material:)

**Framework**: Model I/O  
**Kind**: init

Initializes a submesh with an index buffer and the specified properties.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)
```

#### Return Value

A new submesh object.

#### Discussion

Typically, a submesh is imported from an asset file as a member of a [`MDLMesh`](mdlmesh.md) object, but you can also use this method to create a submesh programmatically.

## Parameters

- `indexBuffer`: An object that provides index data for the submesh.
- `indexCount`: The number of indices in the index buffer.
- `indexType`: The data type of each index in the index buffer.
- `geometryType`: The type of geometric primitives described by the index buffer.
- `material`: A description of the intended surface appearance for rendering the submesh.

## See Also

- [init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:).md)
  Initializes a named submesh with an index buffer and the specified properties.
- [init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?, topology: MDLSubmeshTopology?)](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:topology:).md)
  Initializes a named submesh with a specific topology.
- [init?(mdlSubmesh: MDLSubmesh, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType)](mdlsubmesh/init(mdlsubmesh:indextype:geometrytype:).md)
  Initializes a submesh by copying or converting another submesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/init(indexbuffer:indexcount:indextype:geometrytype:material:))*