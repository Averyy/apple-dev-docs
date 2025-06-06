# init(name:indexBuffer:indexCount:indexType:geometryType:material:topology:)

**Framework**: Model I/O  
**Kind**: init

Initializes a named submesh with a specific topology.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?, topology: MDLSubmeshTopology?)
```

#### Return Value

A new submesh object.

#### Discussion

Typically, a submesh is imported from an asset file as a member of a [`MDLMesh`](mdlmesh.md) object, but you can also use this method to create a submesh programmatically.

Use this method when the index buffer from which you’re creating a submesh does not contain a uniform array of geometric primitives. Pass  [`MDLGeometryType.variableTopology`](mdlgeometrytype/variabletopology.md) for the `geometryType` parameter, and provide an `MDLSubmeshTopology` object for the `topology` parameter to describe how the points in the index buffer combine to produce the submesh’s shape. Otherwise, this method is equivalent to the [`init(name:indexBuffer:indexCount:indexType:geometryType:material:)`](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:).md) method.

## Parameters

- `name`: A descriptive name for the submesh. This property is not used in rendering, but can be useful in debugging.
- `indexBuffer`: An object that provides index data for the submesh.
- `indexCount`: The number of indices in the index buffer.
- `indexType`: The data type of each index in the index buffer.
- `geometryType`: The type of geometric primitives described by the index buffer.
- `material`: A description of the intended surface appearance for rendering the submesh.
- `topology`: An object describing the arrangement of geometric primitives in the index buffer.

## See Also

- [init(indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)](mdlsubmesh/init(indexbuffer:indexcount:indextype:geometrytype:material:).md)
  Initializes a submesh with an index buffer and the specified properties.
- [init(name: String, indexBuffer: any MDLMeshBuffer, indexCount: Int, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType, material: MDLMaterial?)](mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:).md)
  Initializes a named submesh with an index buffer and the specified properties.
- [init?(mdlSubmesh: MDLSubmesh, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType)](mdlsubmesh/init(mdlsubmesh:indextype:geometrytype:).md)
  Initializes a submesh by copying or converting another submesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/init(name:indexbuffer:indexcount:indextype:geometrytype:material:topology:))*