# generateSTMap(device:cameraEye:stmapType:into:)

**Framework**: Immersive Media Support  
**Kind**: method

Generates an STMap for the given projection type and for the given camera eye into the provided texture asynchronously.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func generateSTMap(device: any MTLDevice, cameraEye: ImmersiveLensDefinition.Eye, stmapType: ImmersiveLensDefinition.STMapType, into texture: any MTLTexture) async throws
```

## Parameters

- `device`: The metal device to use during the STMap generation.
- `cameraEye`: The camera side to use for generating the STMap.
- `stmapType`: The type of STMap output: Equirectangular or Equidistant are the current options.
- `texture`: The output texture where the STMap will be stored.

## See Also

- [func encode(to: any Encoder) throws](immersivelensdefinition/encode(to:).md)
  Encodes this value into the given encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivelensdefinition/generatestmap(device:cameraeye:stmaptype:into:))*