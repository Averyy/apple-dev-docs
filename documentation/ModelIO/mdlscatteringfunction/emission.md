# emission

**Framework**: Model I/O  
**Kind**: property

The color emitted as radiance from a material’s surface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emission: MDLMaterialProperty { get }
```

#### Discussion

A renderer (or other software component processing the material) might not treat the emission channel of a material as a light source illuminating the scene. Instead, an emission channel prevents affected areas of a surface from being darkened by other aspects of lighting and shading.

The default emission color is light gray (80% white).

## See Also

- [var baseColor: MDLMaterialProperty](mdlscatteringfunction/basecolor.md)
  The inherent color of the material, to be used as a modulator during shading.
- [var specular: MDLMaterialProperty](mdlscatteringfunction/specular.md)
  The intensity of specular highlights on the material’s surface.
- [var materialIndexOfRefraction: MDLMaterialProperty](mdlscatteringfunction/materialindexofrefraction.md)
  The index of refraction for the medium surrounding a material.
- [var interfaceIndexOfRefraction: MDLMaterialProperty](mdlscatteringfunction/interfaceindexofrefraction.md)
  The index of refraction for a material itself.
- [var normal: MDLMaterialProperty](mdlscatteringfunction/normal.md)
  The variation in the surface normal vectors in a material, relative to model coordinate space.
- [var ambientOcclusion: MDLMaterialProperty](mdlscatteringfunction/ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.
- [var ambientOcclusionScale: MDLMaterialProperty](mdlscatteringfunction/ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction/emission)*