# Vertex Attributes

**Framework**: Model I/O

Names that identify semantic uses for vertex attribute data, used by the [`name`](mdlvertexattribute/name.md) property.

#### Overview

Model I/O  automatically uses these names to identify vertex attribute data loaded from an asset when the asset does not already use its own custom names for vertex attributes.

Some mesh operations require that an attribute with a specific name be present in the mesh. For example, the [`addNormals(withAttributeNamed:creaseThreshold:)`](mdlmesh/addnormals(withattributenamed:creasethreshold:).md) method requires an attribute with the name [`MDLVertexAttributePosition`](mdlvertexattributeposition.md).

## Topics

### Constants
- [let MDLVertexAttributeAnisotropy: String](mdlvertexattributeanisotropy.md)
  The attribute data describes the degree to which a surface’s appearance changes in appearance when rotated about its normal vector.
- [let MDLVertexAttributeBinormal: String](mdlvertexattributebinormal.md)
  The attribute data describes surface binormal vectors.
- [let MDLVertexAttributeBitangent: String](mdlvertexattributebitangent.md)
  The attribute data describes surface bitangent vectors.
- [let MDLVertexAttributeColor: String](mdlvertexattributecolor.md)
  The attribute data describes vertex colors.
- [let MDLVertexAttributeEdgeCrease: String](mdlvertexattributeedgecrease.md)
  The attribute data describes edges that should be left unmodified by surface subdivision operations.
- [let MDLVertexAttributeJointIndices: String](mdlvertexattributejointindices.md)
  The attribute data describes the indices of bones or joints in a skeletal animation rig.
- [let MDLVertexAttributeJointWeights: String](mdlvertexattributejointweights.md)
  The attribute data describes the influence factors of bones or joints on a vertex’s position for use in skeletal animation.
- [let MDLVertexAttributeNormal: String](mdlvertexattributenormal.md)
  The attribute data describes surface normal vectors.
- [let MDLVertexAttributeOcclusionValue: String](mdlvertexattributeocclusionvalue.md)
  The attribute data describes per-vertex ambient occlusion values.
- [let MDLVertexAttributePosition: String](mdlvertexattributeposition.md)
  The attribute data describes vertex positions.
- [let MDLVertexAttributeShadingBasisU: String](mdlvertexattributeshadingbasisu.md)
  The attribute data describes the U component of a vector basis for use in shading.
- [let MDLVertexAttributeShadingBasisV: String](mdlvertexattributeshadingbasisv.md)
  The attribute data describes the V component of a vector basis for use in shading.
- [let MDLVertexAttributeSubdivisionStencil: String](mdlvertexattributesubdivisionstencil.md)
  The attribute data describes which neighboring vertices influence the effect of surface subdivision on the area around a vertex.
- [let MDLVertexAttributeTangent: String](mdlvertexattributetangent.md)
  The attribute data describes surface tangent vectors.
- [let MDLVertexAttributeTextureCoordinate: String](mdlvertexattributetexturecoordinate.md)
  The attribute data describes texture coordinates.

## See Also

- [enum MDLVertexFormat](mdlvertexformat.md)
  Descriptions of the data size and layout for a vertex attribute, used by the [`format`](mdlvertexattribute/format.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/vertex-attributes)*