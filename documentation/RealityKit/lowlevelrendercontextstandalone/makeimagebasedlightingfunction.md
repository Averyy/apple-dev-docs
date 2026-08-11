# makeImageBasedLightingFunction()

**Framework**: RealityKit  
**Kind**: method

Returns a lighting function using image-based lighting (IBL).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeImageBasedLightingFunction() -> sending LowLevelMaterialResource.LightingFunction
```

#### Return Value

An image-based [`LowLevelMaterialResource.LightingFunction`](lowlevelmaterialresource/lightingfunction.md).

#### Discussion

The lighting function expects two cubemap textures bound via its corresponding [`LowLevelArgumentTable`](lowlevelargumenttable.md): one for diffuse and one for specular. Prepare these using [`ImageBasedLightTextureGenerator.generateDiffuse(using:fromSkyboxCube:quality:into:)`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator/generatediffuse(using:fromskyboxcube:quality:into:)) and [`ImageBasedLightTextureGenerator.generateSpecular(using:fromSkyboxCube:quality:into:)`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/imagebasedlighttexturegenerator/generatespecular(using:fromskyboxcube:quality:into:)).

## See Also

- [func makeUnlitLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextstandalone/makeunlitlightingfunction.md)
  Returns an unlit lighting function that emits the surface emissive color directly, without any lighting calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makeimagebasedlightingfunction())*