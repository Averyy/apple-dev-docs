# normal

**Framework**: Model I/O  
**Kind**: property

The variation in the surface normal vectors in a material, relative to model coordinate space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var normal: MDLMaterialProperty { get }
```

#### Discussion

The default normal value is zero (no variation in surface normal vectors). Typically, you assign a texture to this material property to create the appearance of detailed surface contours.

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
- [var ambientOcclusion: MDLMaterialProperty](mdlscatteringfunction/ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.
- [var ambientOcclusionScale: MDLMaterialProperty](mdlscatteringfunction/ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction/normal)*