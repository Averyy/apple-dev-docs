# mip(slices:)

**Framework**: RealityKit  
**Kind**: method

Specifies a single mipmap level of a 2D or 3D texture resource that slices provide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static func mip(slices: [TextureResource.Contents.Slice]) -> TextureResource.Contents.MipmapLevel
```

## Parameters

- `slices`: The source slices.   A 2D array texture requires one slice per  .   A cube texture requires six slices, containing faces  .   2D and 3D textures need a single slice, and you can build their   with    or  .

## See Also

- [static func mip(data: Data, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(data:bytesperrow:).md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(data: Data, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(data:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:).md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/mipmaplevel/mip(slices:))*