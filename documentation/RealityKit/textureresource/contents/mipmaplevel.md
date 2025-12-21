# TextureResource.Contents.MipmapLevel

**Framework**: RealityKit  
**Kind**: struct

An object that references the pixel data for a single mipmap of a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct MipmapLevel
```

## Topics

### Creating a texture mipmap level
- [static func mip(data: Data, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(data:bytesperrow:).md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(data: Data, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(data:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(slices: [TextureResource.Contents.Slice]) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(slices:).md)
  Specifies a single mipmap level of a 2D or 3D texture resource that slices provide.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:).md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TextureResource.Contents.Slice](textureresource/contents/slice.md)
  An object that references the pixel data for a single slice of a mipmap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/mipmaplevel)*