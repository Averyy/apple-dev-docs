# TextureResource.Contents.MipmapLevel

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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
- [static func mip(data: Data, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](./mipmaplevel/mip%28data,bytesperrow%29.md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(data: Data, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](./mipmaplevel/mip%28data,bytesperrow,bytesperimage%29.md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(slices: [TextureResource.Contents.Slice]) -> TextureResource.Contents.MipmapLevel](./mipmaplevel/mip%28slices%29.md)
  Specifies a single mipmap level of a 2D or 3D texture resource that slices provide.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](./mipmaplevel/mip%28unsafebuffer,offset,size,bytesperrow%29.md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](./mipmaplevel/mip%28unsafebuffer,offset,size,bytesperrow,bytesperimage%29.md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Defining the content
- [TextureResource.Contents.Slice](./slice.md)
  An object that references the pixel data for a single slice of a mipmap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/mipmaplevel)*