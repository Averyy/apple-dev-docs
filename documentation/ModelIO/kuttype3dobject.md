# kUTType3dObject

**Framework**: Model I/O  
**Kind**: var

The Object file format (common extension `.obj`).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kUTType3dObject: String
```

#### Discussion

When importing assets in this file format, Model I/O also implements materials from companion files in `.mtl` format. Paths to MTL files are assumed to be relative to the referencing OBJ file, and paths to textures are assumed to be relative to the referencing MTL file.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/kuttype3dobject)*