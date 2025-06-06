# init(from:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a texture resource from a low-level texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from texture: LowLevelTexture) async throws
```

## Parameters

- `texture`: The texture data that defines the resource.

## See Also

- [convenience init(from: LowLevelTexture) throws](textureresource/init(from:)-3psmc.md)
  Synchronously creates a texture resource from a low-level texture.
- [TextureResource.Contents](textureresource/contents.md)
  An object that references the pixel data for each mipmap level of a texture.
- [TextureResource.Format](textureresource/format.md)
  The pixel format and encoding of a texture.
- [TextureResource.Compression](textureresource/compression.md)
  The compression to apply when importing an image as a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(from:)-42r55)*