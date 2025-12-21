# generateMipmaps(texture:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that generates mipmaps for a texture instance from the base mipmap level up to the highest mipmap level.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func generateMipmaps(texture: any MTLTexture)
```

#### Discussion

This method generates mipmaps for a mipmapped texture. The texture you provide needs to have a [`mipmapLevelCount`](mtltexture/mipmaplevelcount.md) greater than `1`, and a color-renderable or color-filterable [`pixelFormat`](mtltexture/pixelformat.md).

## Parameters

- `texture`: A mipmapped, color-renderable or color-filterable   instance the command generates mipmaps for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/generatemipmaps(texture:))*