# baseColor

**Framework**: Model I/O  
**Kind**: property

The inherent color of the material, to be used as a modulator during shading.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var baseColor: MDLMaterialProperty { get }
```

#### Discussion

The default base color is medium gray (50% white).

## See Also

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
- [var ambientOcclusion: MDLMaterialProperty](mdlscatteringfunction/ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.
- [var ambientOcclusionScale: MDLMaterialProperty](mdlscatteringfunction/ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction/basecolor)*