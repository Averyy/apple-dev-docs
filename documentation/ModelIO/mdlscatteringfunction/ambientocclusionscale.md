# ambientOcclusionScale

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The scaling factor for ambient occlusion shading.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var ambientOcclusionScale: MDLMaterialProperty { get }
```

```objc
@property (nonatomic, retain, readonly) MDLMaterialProperty * ambientOcclusionScale;
```

#### Discussion

The default scaling factor is `1.0`. Modify this value to increase or decrease the severity of ambient occlusion shading.

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
- [var interfaceIndexOfRefraction: MDLMaterialProperty](./interfaceindexofrefraction.md)
  The index of refraction for a material itself.
- [var normal: MDLMaterialProperty](./normal.md)
  The variation in the surface normal vectors in a material, relative to model coordinate space.
- [var ambientOcclusion: MDLMaterialProperty](./ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction/ambientocclusionscale)*