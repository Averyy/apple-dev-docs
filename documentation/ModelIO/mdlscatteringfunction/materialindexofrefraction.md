# materialIndexOfRefraction

**Framework**: Model I/O  
**Kind**: property

The index of refraction for the medium surrounding a material.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var materialIndexOfRefraction: MDLMaterialProperty { get }
```

#### Discussion

This value corresponds to the `n1` parameter in Schlick’s equation for approximating Fresnel reflection effects. Typically, one assumes a the medium surrounding a material is air or empty space, so the default value of `1.0` suffices for most uses of this semantic.

## See Also

- [var baseColor: MDLMaterialProperty](mdlscatteringfunction/basecolor.md)
  The inherent color of the material, to be used as a modulator during shading.
- [var emission: MDLMaterialProperty](mdlscatteringfunction/emission.md)
  The color emitted as radiance from a material’s surface.
- [var specular: MDLMaterialProperty](mdlscatteringfunction/specular.md)
  The intensity of specular highlights on the material’s surface.
- [var interfaceIndexOfRefraction: MDLMaterialProperty](mdlscatteringfunction/interfaceindexofrefraction.md)
  The index of refraction for a material itself.
- [var normal: MDLMaterialProperty](mdlscatteringfunction/normal.md)
  The variation in the surface normal vectors in a material, relative to model coordinate space.
- [var ambientOcclusion: MDLMaterialProperty](mdlscatteringfunction/ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.
- [var ambientOcclusionScale: MDLMaterialProperty](mdlscatteringfunction/ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction/materialindexofrefraction)*