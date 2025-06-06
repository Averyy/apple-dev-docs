# TextureResource.MipmapsMode

**Framework**: RealityKit  
**Kind**: enum

An enumeration for specifying how to allocate and generate mipmaps for a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
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
### Comparing enumeration values
- [var hashValue: Int](textureresource/mipmapsmode/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](textureresource/mipmapsmode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func == (TextureResource.MipmapsMode, TextureResource.MipmapsMode) -> Bool](textureresource/mipmapsmode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](textureresource/mipmapsmode/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](textureresource/mipmapsmode/equatable-implementations.md)

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
- [TextureResource.Semantic](textureresource/semantic-swift.enum.md)
  An object for specifying the intended use of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/mipmapsmode)*