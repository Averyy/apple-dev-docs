# makeImageBasedLightingFunction()

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Returns a lighting function using image-based lighting (IBL).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeImageBasedLightingFunction() -> sending LowLevelMaterialResource.LightingFunction
```

#### Return Value

An image-based [`LowLevelMaterialResource.LightingFunction`](lowlevelmaterialresource/lightingfunction.md).

#### Discussion

The lighting function expects two cubemap textures bound via its corresponding [`LowLevelArgumentTable`](lowlevelargumenttable.md): one for diffuse and one for specular. Prepare these using `LowLevelTextureProcessingContext/generateImageBasedLightDiffuse` and `LowLevelTextureProcessingContext/generateImageBasedLightSpecular`.

## See Also

- [func makeUnlitLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextlighting/makeunlitlightingfunction.md)
  Returns an unlit lighting function that emits the surface emissive color directly, without any lighting calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextlighting/makeimagebasedlightingfunction())*