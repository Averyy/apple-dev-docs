# minimumTextureBufferAlignment(for:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (NSUInteger) minimumTextureBufferAlignmentForPixelFormat:(MTLPixelFormat) format;
```

#### Discussion

Metal aligns textures to their minimum alignment value, which directly affects the [`makeTexture(descriptor:offset:bytesPerRow:)`](../mtlbuffer/maketexture%28descriptor,offset,bytesperrow%29.md) method’s `offset` and `bytesPerRow` parameters.

## Parameters

- `format`: An [`MTLPixelFormat`](../mtlpixelformat.md) instance.

## See Also

### Creating textures
- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](./maketexture%28descriptor%29.md)
  Creates a new texture instance.
- [func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?](./maketexture%28descriptor,iosurface,plane%29.md)
  Creates a texture instance that uses I/O surface to store its underlying data.
- [func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](./makesharedtexture%28descriptor%29.md)
  Creates a texture that you can share across process boundaries.
- [func makeSharedTexture(handle: MTLSharedTextureHandle) -> (any MTLTexture)?](./makesharedtexture%28handle%29.md)
  Creates a texture that references a shared texture.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](./minimumlineartexturealignment%28for%29.md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/minimumtexturebufferalignment(for:))*