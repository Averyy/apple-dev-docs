# TextureResource.Semantic

**Framework**: RealityKit  
**Kind**: enum

An object for specifying the intended use of a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
enum Semantic
```

#### Overview

RealityKit uses image textures to transmit different types of data Metal shaders. For example, it uses textures to send RGB images with the base color of the entity, to send grayscale images holding roughness and metallic information, and to send surface normals for doing lighting calculations.

This object specifies the intended use of the texture by an individual property.

## Topics

### Specifying intended use
- [TextureResource.Semantic.raw](textureresource/semantic-swift.enum/raw.md)
  Use the texture unmodified.
- [TextureResource.Semantic.color](textureresource/semantic-swift.enum/color.md)
  Use the texture to store colors data.
- [TextureResource.Semantic.hdrColor](textureresource/semantic-swift.enum/hdrcolor.md)
  Use the texture to store a high-dynamic range image.
- [TextureResource.Semantic.normal](textureresource/semantic-swift.enum/normal.md)
  Use the texture to store surface normals.
- [TextureResource.Semantic.scalar](textureresource/semantic-swift.enum/scalar.md)
  Use the texture to store a single value in each pixel.
### Comparing enumeration values
- [var hashValue: Int](textureresource/semantic-swift.enum/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](textureresource/semantic-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func == (TextureResource.Semantic, TextureResource.Semantic) -> Bool](textureresource/semantic-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](textureresource/semantic-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](textureresource/semantic-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class TextureResource](textureresource.md)
  A representation of a texture.
- [TextureResource.CreateOptions](textureresource/createoptions.md)
  An object that holds texture resource creation options.
- [TextureResource.SamplingQuality](textureresource/samplingquality.md)
  An object for controlling the texture-sampling quality.
- [TextureResource.MipmapsMode](textureresource/mipmapsmode.md)
  An enumeration for specifying how to allocate and generate mipmaps for a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/semantic-swift.enum)*