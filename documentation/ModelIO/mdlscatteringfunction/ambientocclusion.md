# ambientOcclusion

**Framework**: Model I/O  
**Kind**: property

The attenuation of ambient light due to local geometry variations on a surface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var ambientOcclusion: MDLMaterialProperty { get }
```

#### Discussion

Ambient occlusion (AO) describes the accessibility of a point on a surface to the surrounding radiant environment and is typically used to attenuate ambient lighting. A renderer should not use AO data should to affect direct illumination.

The default AO value is zero. Typically, you assign a texture (such as that created with the [`generateAmbientOcclusionTexture(withQuality:attenuationFactor:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:)`](mdlmesh/generateambientocclusiontexture(withquality:attenuationfactor:objectstoconsider:vertexattributenamed:materialpropertynamed:).md) method of a mesh) to this material property to add shading based on the shape of the mesh.

## See Also

- [var baseColor: MDLMaterialProperty](mdlscatteringfunction/basecolor.md)
  The inherent color of the material, to be used as a modulator during shading.
- [var emission: MDLMaterialProperty](mdlscatteringfunction/emission.md)
  The color emitted as radiance from a material’s surface.
- [var specular: MDLMaterialProperty](mdlscatteringfunction/specular.md)
  The intensity of specular highlights on the material’s surface.
- [var materialIndexOfRefraction: MDLMaterialProperty](mdlscatteringfunction/materialindexofrefraction.md)
  The index of refraction for the medium surrounding a material.
- [var interfaceIndexOfRefraction: MDLMaterialProperty](mdlscatteringfunction/interfaceindexofrefraction.md)
  The index of refraction for a material itself.
- [var normal: MDLMaterialProperty](mdlscatteringfunction/normal.md)
  The variation in the surface normal vectors in a material, relative to model coordinate space.
- [var ambientOcclusionScale: MDLMaterialProperty](mdlscatteringfunction/ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction/ambientocclusion)*