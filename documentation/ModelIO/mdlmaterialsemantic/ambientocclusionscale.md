# MDLMaterialSemantic.ambientOcclusionScale

**Framework**: Model I/O  
**Kind**: case

The scaling factor for ambient occlusion shading.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case ambientOcclusionScale
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/ambientocclusionscale)*