# mip(data:bytesPerRow:)

**Framework**: RealityKit  
**Kind**: method

Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
static func mip(data: Data, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel
```

## Parameters

- `data`: The source buffer.
- `bytesPerRow`: The stride in bytes between rows of texture data that RealityKit stores in the source buffer.   The value needs to be a multiple of the destination texture’s pixel size, in bytes.

## See Also

- [static func mip(data: Data, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(data:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(slices: [TextureResource.Contents.Slice]) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(slices:).md)
  Specifies a single mipmap level of a 2D or 3D texture resource that slices provide.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:).md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:bytesperimage:).md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/mipmaplevel/mip(data:bytesperrow:))*