# mip(data:bytesPerRow:bytesPerImage:)

**Framework**: RealityKit  
**Kind**: method

Specifies a multi-image mipmap level of a texture resource with pixel data that RealityKit copies from a byte buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 2.0+

## Declaration

```swift
static func mip(data: Data, bytesPerRow: Int, bytesPerImage: Int) -> TextureResource.Contents.MipmapLevel
```

## Parameters

- `data`: The source buffer.
- `bytesPerRow`: The stride in bytes between rows of texture data that RealityKit stores in the source buffer.   The value needs to be a multiple of the destination texture’s pixel size, in bytes.
- `bytesPerImage`: The stride in bytes between image planes of texture data that RealityKit stores in the source buffer,   needed for 3D texture mipmaps.   The value needs to be a multiple of the destination texture’s   pixel size, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents-179q2/mipmaplevel/mip(data:bytesperrow:bytesperimage:))*