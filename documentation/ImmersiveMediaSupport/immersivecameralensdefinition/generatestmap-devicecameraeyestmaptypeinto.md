# generateSTMap(device:cameraEye:stmapType:into:)

**Framework**: Immersive Media Support  
**Kind**: method

Generates an STMap for the given projection type and for the given camera eye into the provided texture asynchronously.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func generateSTMap(device: any MTLDevice, cameraEye: ImmersiveCameraLensDefinition.Eye, stmapType: ImmersiveCameraLensDefinition.STMapType, into texture: any MTLTexture) async throws
```

## Parameters

- `device`: The metal device to use during the STMap generation.
- `cameraEye`: The camera side to use for generating the STMap.
- `stmapType`: The type of STMap output: Equirectangular or Equidistant are the current options.
- `texture`: The output texture where the STMap will be stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameralensdefinition/generatestmap(device:cameraeye:stmaptype:into:))*