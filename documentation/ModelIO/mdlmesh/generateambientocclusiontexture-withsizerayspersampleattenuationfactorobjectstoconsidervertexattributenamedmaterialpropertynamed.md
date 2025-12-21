# generateAmbientOcclusionTexture(withSize:raysPerSample:attenuationFactor:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:)

**Framework**: Model I/O  
**Kind**: method

Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a material property texture of the specified size.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func generateAmbientOcclusionTexture(withSize textureSize: vector_int2, raysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if AO calculation succeeded; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Ambient occlusion (AO) is a measure, for each point on a surface, of how much ambient light can reach that point. For example, a narrow, concave section of a mesh does not receive much ambient light compared with a wide, flat section—thus, in a realistic rendering of the mesh, the concave sections should appear darker than the flat sections. This method analyzes the mesh (and, optionally, static elements of its local environment, specified in the `objectsToConsider` parameter) to precompute (or “bake”) AO information for each point on the mesh’s surface. You can then use the resulting information in shading to produce a more realistic render.

This method saves AO data as a texture image and associates that image with the mesh through the material property specified in the `materialPropertyName` parameter. To map the texture onto the mesh’s surface, this method also generates texture coordinates and writes them in the vertex attribute specified in the `vertexAttributeName` parameter. If the mesh already contains that attribute, this method overwrites the contents of the corresponding vertex buffer. If the mesh does not contain that attribute, this method creates a new attribute and updates the mesh’s [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) object accordingly.

The `textureSize` and `raysPerSample` parameters together control the fidelity and performance of the AO calculation process and its output. To control quality without specifying a texture size or raytracing options, use the [`generateAmbientOcclusionTexture(withQuality:attenuationFactor:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:)`](mdlmesh/generateambientocclusiontexture(withquality:attenuationfactor:objectstoconsider:vertexattributenamed:materialpropertynamed:).md) method.

## Parameters

- `textureSize`: The size of texture image to generate.
- `raysPerSample`: The number of rays to trace for each texel in the generated texture to test for potential occlusion. Higher numbers produce more accurate output at the cost of more processing time and memory usage.
- `attenuationFactor`: A value between   and   that scales the strength of the AO effect. Higher values result in higher contrast when the AO texture is used for shading.
- `objectsToConsider`: An array of other objects in the scene that should affect static ambient lighting for the mesh.
- `vertexAttributeName`: The name of the vertex attribute for storing generated texture coordinate data.
- `materialPropertyName`: The name of the material for storing the generated texture image.

## See Also

- [func generateAmbientOcclusionTexture(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](mdlmesh/generateambientocclusiontexture(withquality:attenuationfactor:objectstoconsider:vertexattributenamed:materialpropertynamed:).md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a material property texture.
- [func generateAmbientOcclusionVertexColors(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](mdlmesh/generateambientocclusionvertexcolors(withquality:attenuationfactor:objectstoconsider:vertexattributenamed:).md)
  Calculates ambient occlusion (AO) information for the mesh and saves it in the mesh as a vertex color attribute.
- [func generateAmbientOcclusionVertexColors(withRaysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](mdlmesh/generateambientocclusionvertexcolors(withrayspersample:attenuationfactor:objectstoconsider:vertexattributenamed:).md)
  Calculates ambient occlusion (AO) information for the mesh, using the specified number of rays per sample, and saves it in the mesh as a vertex color attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/generateambientocclusiontexture(withsize:rayspersample:attenuationfactor:objectstoconsider:vertexattributenamed:materialpropertynamed:))*