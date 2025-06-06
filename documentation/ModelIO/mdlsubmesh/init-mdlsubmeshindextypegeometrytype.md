# init(mdlSubmesh:indexType:geometryType:)

**Framework**: Model I/O  
**Kind**: init

Initializes a submesh by copying or converting another submesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init?(mdlSubmesh submesh: MDLSubmesh, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType)
```

#### Return Value

A new submesh object.

#### Discussion

If the `indexType` or `geometryType` parameter does not match the corresponding property of the object in the `submesh` parameter, this method creates a new index buffer by converting the submesh’s index buffer to the described format while preserving shape and topology. For example, you can use this method to convert a quad mesh to a triangle mesh for rendering using GPUs that do not support quad primitives, or to convert a triangle mesh to triangle strips to create a smaller index buffer.

If the `indexType` and `geometryType` parameters match the corresponding properties of the input submesh, this method simply copies that submesh’s index buffer to create the new submesh.

## Parameters

- `submesh`: The submesh to copy or convert from.
- `indexType`: The data type of each index for the new submesh’s index buffer.
- `geometryType`: The type of geometric primitives for the new submesh’s index buffer.

## See Also

- [init(indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)](mdlsubmesh/init(indexbuffer:indexcount:indextype:geometrytype:material:).md)
  Initializes a submesh with an index buffer and the specified properties.
- [init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:).md)
  Initializes a named submesh with an index buffer and the specified properties.
- [init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?, topology: MDLSubmeshTopology?)](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:topology:).md)
  Initializes a named submesh with a specific topology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/init(mdlsubmesh:indextype:geometrytype:))*