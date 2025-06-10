# MDLMaterialSemantic

**Framework**: Model I/O  
**Kind**: enum

Options for the semantic use of a material property’s value in rendering a particular surface appearance; used by the [`semantic`](mdlmaterialproperty/semantic.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLMaterialSemantic
```

## Topics

### Constants
- [MDLMaterialSemantic.baseColor](mdlmaterialsemantic/basecolor.md)
  The inherent color of a surface, to be used as a modulator during shading.
- [MDLMaterialSemantic.subsurface](mdlmaterialsemantic/subsurface.md)
  The degree to which light scatters under the surface of a material.
- [MDLMaterialSemantic.metallic](mdlmaterialsemantic/metallic.md)
  The degree to which a material appears as a dielectric surface (lower values) or as a metal (higher values).
- [MDLMaterialSemantic.specular](mdlmaterialsemantic/specular.md)
  The intensity of specular highlights that appear on the material’s surface.
- [MDLMaterialSemantic.specularExponent](mdlmaterialsemantic/specularexponent.md)
  The exponent to be used in Blinn-Phong approximation of the material’s specular response.
- [MDLMaterialSemantic.specularTint](mdlmaterialsemantic/speculartint.md)
  The balance of color for specular highlights, between the light color (lower values) and the material’s base color (at higher values).
- [MDLMaterialSemantic.roughness](mdlmaterialsemantic/roughness.md)
  The degree to which a material appears smooth, affecting both diffuse and specular response.
- [MDLMaterialSemantic.anisotropic](mdlmaterialsemantic/anisotropic.md)
  The degree to which specular highlights elongate in the direction of the local tangent basis.
- [MDLMaterialSemantic.anisotropicRotation](mdlmaterialsemantic/anisotropicrotation.md)
  The angle at which anisotropic effects are rotated relative to the local tangent basis.
- [MDLMaterialSemantic.sheen](mdlmaterialsemantic/sheen.md)
  The intensity of highlights that appear only at glancing angles on a material’s surface.
- [MDLMaterialSemantic.sheenTint](mdlmaterialsemantic/sheentint.md)
  The balance of color for highlights that appear only at glancing angles, between the light color (lower values) and the material’s base color (at higher values).
- [MDLMaterialSemantic.clearcoat](mdlmaterialsemantic/clearcoat.md)
  The intensity of a second specular highlight, similar to the gloss that results from a clear coat on an automotive finish.
- [MDLMaterialSemantic.clearcoatGloss](mdlmaterialsemantic/clearcoatgloss.md)
  The spread of a second specular highlight, similar to the gloss that results from a clear coat on an automotive finish.
- [MDLMaterialSemantic.emission](mdlmaterialsemantic/emission.md)
  The color emitted as radiance from a material’s surface.
- [MDLMaterialSemantic.bump](mdlmaterialsemantic/bump.md)
  The degree of perturbation in a material’s surface.
- [MDLMaterialSemantic.opacity](mdlmaterialsemantic/opacity.md)
  The opacity of a material’s surface.
- [MDLMaterialSemantic.interfaceIndexOfRefraction](mdlmaterialsemantic/interfaceindexofrefraction.md)
  The index of refraction for the medium surrounding a material.
- [MDLMaterialSemantic.materialIndexOfRefraction](mdlmaterialsemantic/materialindexofrefraction.md)
  The index of refraction for a material itself.
- [MDLMaterialSemantic.objectSpaceNormal](mdlmaterialsemantic/objectspacenormal.md)
  The variation in the surface normal vectors in a material, relative to model coordinate space.
- [MDLMaterialSemantic.tangentSpaceNormal](mdlmaterialsemantic/tangentspacenormal.md)
  The variation in the surface normal vectors in a material, relative to surface tangent coordinate space.
- [MDLMaterialSemantic.displacement](mdlmaterialsemantic/displacement.md)
  The displacement of a material’s surface relative to the surface normal.
- [MDLMaterialSemantic.displacementScale](mdlmaterialsemantic/displacementscale.md)
  The scaling factor for displacement of a material’s surface.
- [MDLMaterialSemantic.ambientOcclusion](mdlmaterialsemantic/ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.
- [MDLMaterialSemantic.ambientOcclusionScale](mdlmaterialsemantic/ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.
- [MDLMaterialSemantic.none](mdlmaterialsemantic/none.md)
  The material property’s [`semantic`](mdlmaterialproperty/semantic.md) property has not been initialized.
- [MDLMaterialSemantic.userDefined](mdlmaterialsemantic/userdefined.md)
  The meaning of the material property’s value is not one of the standard semantic uses recognized by Model I/O.
### Initializers
- [init?(rawValue: UInt)](mdlmaterialsemantic/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MDLMaterialPropertyType](mdlmaterialpropertytype.md)
  Options for the data type of a material property, used by the [`type`](mdlmaterialproperty/type.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic)*