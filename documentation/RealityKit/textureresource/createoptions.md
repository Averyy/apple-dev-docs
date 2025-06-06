# TextureResource.CreateOptions

**Framework**: RealityKit  
**Kind**: struct

An object that holds texture resource creation options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct CreateOptions
```

## Topics

### Texture resource initializers
- [init(semantic: TextureResource.Semantic?, mipmapsMode: TextureResource.MipmapsMode)](textureresource/createoptions/init(semantic:mipmapsmode:).md)
  Creates a texture creation options structure.
### Texture resource creation options
- [var mipmapsMode: TextureResource.MipmapsMode](textureresource/createoptions/mipmapsmode.md)
  Whether the texture resource automatically generates mipmaps.
- [var semantic: TextureResource.Semantic?](textureresource/createoptions/semantic.md)
  The intended use of the texture.
### Initializers
- [init(semantic: TextureResource.Semantic?, compression: TextureResource.Compression, mipmapsMode: TextureResource.MipmapsMode)](textureresource/createoptions/init(semantic:compression:mipmapsmode:).md)
  Creates a texture creation options structure.
### Instance Properties
- [var compression: TextureResource.Compression](textureresource/createoptions/compression.md)

## See Also

- [class TextureResource](textureresource.md)
  A representation of a texture.
- [TextureResource.SamplingQuality](textureresource/samplingquality.md)
  An object for controlling the texture-sampling quality.
- [TextureResource.MipmapsMode](textureresource/mipmapsmode.md)
  An enumeration for specifying how to allocate and generate mipmaps for a texture.
- [TextureResource.Semantic](textureresource/semantic-swift.enum.md)
  An object for specifying the intended use of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/createoptions)*