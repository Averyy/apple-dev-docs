# mip(unsafeBuffer:offset:size:bytesPerRow:)

**Framework**: RealityKit  
**Kind**: method

Specifies a single mipmap level of a texture resource with pixel data that RealityKit copies from a Metal buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
static func mip(unsafeBuffer buffer: any MTLBuffer, offset: Int = 0, size: Int, bytesPerRow: Int) -> TextureResource.Contents.MipmapLevel
```

#### Discussion

> ❗ **Important**: A [`TextureResource.Contents.MipmapLevel`](textureresource/contents-179q2/mipmaplevel.md) that you create with this function and use to create a [`TextureResource`](textureresource.md) copies from the source buffer. That copy occurs when initializing the texture resource. The caller is responsible for ensuring that the system doesn’t modify the source Metal buffer while copying it to a texture.

## Parameters

- `buffer`: The source buffer.   Don’t modify this buffer while using it as the source of a copy operation.
- `offset`: The byte position in the source buffer where the copying starts.   The offset needs to be a multiple of the destination texture’s pixel size, in bytes.
- `size`: The number of bytes in the source buffer (starting from  ) available for copying.
- `bytesPerRow`: The stride in bytes between rows of texture data that RealityKit stores in the source buffer.   The value needs to be a multiple of the destination texture’s pixel size, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents-179q2/mipmaplevel/mip(unsafebuffer:offset:size:bytesperrow:))*