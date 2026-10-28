# interfaceIndexOfRefraction

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The index of refraction for a material itself.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var interfaceIndexOfRefraction: MDLMaterialProperty { get }
```

```objc
@property (nonatomic, retain, readonly) MDLMaterialProperty * interfaceIndexOfRefraction;
```

## Discussion

This value corresponds to the `n2` parameter in Schlick’s equation for approximating Fresnel reflection effects.

The default value is `1.0`.

## See Also

### Working with Shading Properties
- [var baseColor: MDLMaterialProperty](./basecolor.md)
  The inherent color of the material, to be used as a modulator during shading.
- [var emission: MDLMaterialProperty](./emission.md)
  The color emitted as radiance from a material’s surface.
- [var specular: MDLMaterialProperty](./specular.md)
  The intensity of specular highlights on the material’s surface.
- [var materialIndexOfRefraction: MDLMaterialProperty](./materialindexofrefraction.md)
  The index of refraction for the medium surrounding a material.
- [var normal: MDLMaterialProperty](./normal.md)
  The variation in the surface normal vectors in a material, relative to model coordinate space.
- [var ambientOcclusion: MDLMaterialProperty](./ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.
- [var ambientOcclusionScale: MDLMaterialProperty](./ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction/interfaceindexofrefraction)*