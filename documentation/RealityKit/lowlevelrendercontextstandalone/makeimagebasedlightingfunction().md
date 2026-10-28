# makeImageBasedLightingFunction()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a lighting function using image-based lighting (IBL).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func makeImageBasedLightingFunction() -> sending LowLevelMaterialResource.LightingFunction
```

## Return Value

An image-based [`LowLevelMaterialResource.LightingFunction`](../lowlevelmaterialresource/lightingfunction.md).

## Discussion

The lighting function expects two cubemap textures bound via its corresponding [`LowLevelArgumentTable`](../lowlevelargumenttable.md): one for diffuse and one for specular. Prepare these using [ImageBasedLightTextureGenerator.generateDiffuse(using:fromSkyboxCube:quality:into:)](../imagebasedlighttexturegenerator/generatediffuse%28using,fromskyboxcube,quality,into%29.md) and [ImageBasedLightTextureGenerator.generateSpecular(using:fromSkyboxCube:quality:into:)](../imagebasedlighttexturegenerator/generatespecular%28using,fromskyboxcube,quality,into%29.md).

## See Also

### Creating lighting functions
- [func makeUnlitLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](./makeunlitlightingfunction%28%29.md)
  Returns an unlit lighting function that emits the surface emissive color directly, without any lighting calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makeimagebasedlightingfunction())*