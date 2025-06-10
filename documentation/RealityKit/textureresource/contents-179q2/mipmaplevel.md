# TextureResource.Contents.MipmapLevel

**Framework**: RealityKit  
**Kind**: struct

An object that references the pixel data for a single mipmap of a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct MipmapLevel
```

## Topics

### Type Methods
- [static mip(data:bytesPerRow:)](textureresource/contents-179q2/mipmaplevel/mip(data:bytesperrow:).md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static mip(data:bytesPerRow:bytesPerImage:)](textureresource/contents-179q2/mipmaplevel/mip(data:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static mip(slices:)](textureresource/contents-179q2/mipmaplevel/mip(slices:).md)
  Specifies a single mipmap level of a 2D or 3D texture resource that slices provide.
- [static mip(unsafeBuffer:offset:size:bytesPerRow:)](textureresource/contents-179q2/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:).md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.
- [static mip(unsafeBuffer:offset:size:bytesPerRow:bytesPerImage:)](textureresource/contents-179q2/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents-179q2/mipmaplevel)*