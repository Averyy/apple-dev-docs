# addTangentBasis(forTextureCoordinateAttributeNamed:tangentAttributeNamed:bitangentAttributeNamed:)

**Framework**: Model I/O  
**Kind**: method

Generates surface tangent and bitangent data for the mesh based on its vertex position and texture coordinate data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addTangentBasis(forTextureCoordinateAttributeNamed textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeName: String, bitangentAttributeNamed bitangentAttributeName: String?)
```

#### Discussion

Surface-space tangent and bitangent vectors can be used to produce shading effects that follow the “flow” of a surface or to generate normal map textures. Model I/O  calculates tangent and bitangent vectors based on vertex positions and texture coordinates using a common definition: The tangent vector at a point is tangent to the surface and parallel to the texture coordinate s-axis, and the bitangent vector is tangent to the surface and parallel to the texture coordinate t-axis.

For this method to calculate surface tangent vectors, the mesh must contain vertex data for both the [`MDLVertexAttributePosition`](mdlvertexattributeposition.md) attribute and the texture coordinate attribute specified in the `textureCoordinateAttributeName` parameter. Calling this method on a mesh that does not contain the specified vertex attributes raises an exception.

This method saves calculated normal data in the vertex attributes named in the `tangentAttributeName` and `bitangentAttributeName` parameters. If the mesh already contains either attribute, this method overwrites the contents of the corresponding vertex buffers. If the mesh does not contain an attribute, this method creates a new attribute and updates the mesh’s [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) object accordingly.

## Parameters

- `textureCoordinateAttributeName`: The name of the vertex attribute from which to read texture coordinate data for use in generating tangent and bitangent vectors.
- `tangentAttributeName`: The name of the vertex attribute for storing surface tangent vector data.
- `bitangentAttributeName`: The name of the vertex attribute for storing surface bitangent vector data.

## See Also

- [func addNormals(withAttributeNamed: String?, creaseThreshold: Float)](mdlmesh/addnormals(withattributenamed:creasethreshold:).md)
  Generates surface normal data for the mesh based on its vertex position data.
- [func addTangentBasis(forTextureCoordinateAttributeNamed: String, normalAttributeNamed: String, tangentAttributeNamed: String)](mdlmesh/addtangentbasis(fortexturecoordinateattributenamed:normalattributenamed:tangentattributenamed:).md)
  Generates surface tangent data for the mesh based on its vertex position, surface normal, and texture coordinate data.
- [func makeVerticesUnique()](mdlmesh/makeverticesunique.md)
  Modifies the mesh’s vertex buffers so that no vertices are shared by multiple faces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/addtangentbasis(fortexturecoordinateattributenamed:tangentattributenamed:bitangentattributenamed:))*