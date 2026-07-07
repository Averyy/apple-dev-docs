# makeUnlitLightingFunction()

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Returns an unlit lighting function that emits the surface emissive color directly, without any lighting calculations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeUnlitLightingFunction() -> sending LowLevelMaterialResource.LightingFunction
```

#### Return Value

An unlit [`LowLevelMaterialResource.LightingFunction`](lowlevelmaterialresource/lightingfunction.md).

## See Also

- [func makeImageBasedLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextlighting/makeimagebasedlightingfunction.md)
  Returns a lighting function using image-based lighting (IBL).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextlighting/makeunlitlightingfunction())*