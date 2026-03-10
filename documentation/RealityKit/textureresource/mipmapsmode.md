# TextureResource.MipmapsMode

**Framework**: RealityKit  
**Kind**: enum

An enumeration for specifying how to allocate and generate mipmaps for a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
enum MipmapsMode
```

## Topics

### Specifying allocation and generation
- [TextureResource.MipmapsMode.none](textureresource/mipmapsmode/none.md)
  Do not allocate mipmaps for the texture resource.
- [TextureResource.MipmapsMode.allocateAll](textureresource/mipmapsmode/allocateall.md)
  Allocate memory for all mipmaps, but don’t generate them.
- [TextureResource.MipmapsMode.allocateAndGenerateAll](textureresource/mipmapsmode/allocateandgenerateall.md)
  Allocate and generate all mipmaps for the texture resource.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Generating procedural textures](../visionOS/generating-procedural-textures-in-visionos.md)
  Display a 3D model that generates procedural textures in a reality view.
- [Displaying a stereoscopic image](../visionOS/displaying-a-stereoscopic-image-in-visionos.md)
  Build a stereoscopic image by applying textures to the left and right eye in a shader graph material.
- [class TextureResource](textureresource.md)
  A representation of a texture.
- [TextureResource.CreateOptions](textureresource/createoptions.md)
  An object that holds texture resource creation options.
- [TextureResource.SamplingQuality](textureresource/samplingquality.md)
  An object for controlling the texture-sampling quality.
- [TextureResource.Semantic](textureresource/semantic-swift.enum.md)
  An object for specifying the intended use of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/mipmapsmode)*