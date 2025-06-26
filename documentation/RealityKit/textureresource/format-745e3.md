# TextureResource.Format

**Framework**: RealityKit  
**Kind**: struct

The pixel format and encoding of a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct Format
```

#### Overview

The texture’s format controls the sampling and conversions (if any) to use when rendering with that texture.

## Topics

### Type Methods
- [static color(_:pixelFormat:)](textureresource/format-745e3/color(_:pixelformat:).md)
  Indicates that a texture contains color data to interpret in a specific color space.
- [static normal(_:pixelFormat:)](textureresource/format-745e3/normal(_:pixelformat:).md)
  Indicates that a texture is a normal map.
- [static raw(pixelFormat:)](textureresource/format-745e3/raw(pixelformat:).md)
  Indicates a texture for unmodified use by a shader.
### Enumerations
- [TextureResource.Format.ColorSpace](textureresource/format-745e3/colorspace.md)
  A profile that specifies the interpretation of pixel values as a color.
- [TextureResource.Format.NormalEncoding](textureresource/format-745e3/normalencoding.md)
  A profile that specifies the interpretation of pixel values as a normal.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format-745e3)*