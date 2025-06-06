# minimumTextureBufferAlignment(for:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func minimumTextureBufferAlignment(for format: MTLPixelFormat) -> Int
```

#### Discussion

Metal aligns textures to their minimum alignment value, which directly affects the [`makeTexture(descriptor:offset:bytesPerRow:)`](mtlbuffer/maketexture(descriptor:offset:bytesperrow:).md) method’s `offset` and `bytesPerRow` parameters.

## Parameters

- `format`: An   instance.

## See Also

- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/maketexture(descriptor:).md)
  Creates a new texture instance.
- [func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?](mtldevice/maketexture(descriptor:iosurface:plane:).md)
  Creates a texture instance that uses I/O surface to store its underlying data.
- [func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/makesharedtexture(descriptor:).md)
  Creates a texture that you can share across process boundaries.
- [func makeSharedTexture(handle: MTLSharedTextureHandle) -> (any MTLTexture)?](mtldevice/makesharedtexture(handle:).md)
  Creates a texture that references a shared texture.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](mtldevice/minimumlineartexturealignment(for:).md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/minimumtexturebufferalignment(for:))*