# slice(data:bytesPerRow:)

**Framework**: RealityKit  
**Kind**: method

Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a byte buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static func slice(data: Data, bytesPerRow: Int) -> TextureResource.Contents.Slice
```

## Parameters

- `data`: The source buffer.
- `bytesPerRow`: The stride in bytes between rows of texture data that RealityKit stores in the source buffer.   The value needs to be a multiple of the destination texture’s pixel size, in bytes.

## See Also

- [static func slice(unsafeBuffer: any MTLBuffer, offset: Int, size: Int, bytesPerRow: Int) -> TextureResource.Contents.Slice](textureresource/contents/slice/slice(unsafebuffer:offset:size:bytesperrow:).md)
  Specifies a single mipmap level slice of a texture resource with pixel data that RealityKit copies from a Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents/slice/slice(data:bytesperrow:))*