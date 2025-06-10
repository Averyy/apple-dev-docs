# encode(to:)

**Framework**: Immersive Media Support  
**Kind**: method

Encodes this value into the given encoder.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

- [func generateSTMap(device: any MTLDevice, cameraEye: ImmersiveLensDefinition.Eye, stmapType: ImmersiveLensDefinition.STMapType, into: any MTLTexture) async throws](immersivelensdefinition/generatestmap(device:cameraeye:stmaptype:into:).md)
  Generates an STMap for the given projection type and for the given camera eye into the provided texture asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivelensdefinition/encode(to:))*