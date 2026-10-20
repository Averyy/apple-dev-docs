# mip(slices:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

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

- `slices`: The source slices. A 2D array texture requires one slice per `arrayLength`. A cube texture requires six slices, containing faces `[+X, -X, +Y, -Y, +Z, -Z]`. 2D and 3D textures need a single slice, and you can build their `MipmapLevel` with `mip(buffer:offset:size:bytesPerRow:)` or `mip(data:bytesPerRow)`.

## See Also

### Creating a texture mipmap level
- [static func mip(data: Data, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](./mip%28data,bytesperrow%29.md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(data: Data, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](./mip%28data,bytesperrow,bytesperimage%29.md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel](./mip%28unsafebuffer,offset,size,bytesperrow%29.md)
  Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.
- [static func mip(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel](./mip%28unsafebuffer,offset,size,bytesperrow,bytesperimage%29.md)
  Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/mipmaplevel/mip(slices:))*