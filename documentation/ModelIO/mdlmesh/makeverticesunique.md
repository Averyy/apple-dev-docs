# makeVerticesUnique()

**Framework**: Model I/O  
**Kind**: method

Modifies the mesh’s vertex buffers so that no vertices are shared by multiple faces.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func makeVerticesUnique()
```

#### Discussion

If the same entry in the mesh’s vertex buffer is used in multiple faces (according to the index buffers of the mesh’s submeshes), this method duplicates that vertex data and modifies the vertex and index buffers accordingly. If such operations require a larger vertex or index buffer, this method uses the [`allocator`](mdlmeshbuffer/allocator.md) property of the buffer in question to allocate new storage.

## See Also

- [func addNormals(withAttributeNamed: String?, creaseThreshold: Float)](mdlmesh/addnormals(withattributenamed:creasethreshold:).md)
  Generates surface normal data for the mesh based on its vertex position data.
- [func addTangentBasis(forTextureCoordinateAttributeNamed: String, tangentAttributeNamed: String, bitangentAttributeNamed: String?)](mdlmesh/addtangentbasis(fortexturecoordinateattributenamed:tangentattributenamed:bitangentattributenamed:).md)
  Generates surface tangent and bitangent data for the mesh based on its vertex position and texture coordinate data.
- [func addTangentBasis(forTextureCoordinateAttributeNamed: String, normalAttributeNamed: String, tangentAttributeNamed: String)](mdlmesh/addtangentbasis(fortexturecoordinateattributenamed:normalattributenamed:tangentattributenamed:).md)
  Generates surface tangent data for the mesh based on its vertex position, surface normal, and texture coordinate data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/makeverticesunique())*