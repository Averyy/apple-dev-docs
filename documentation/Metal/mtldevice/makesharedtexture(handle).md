# makeSharedTexture(handle:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a texture that references a shared texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func makeSharedTexture(handle sharedHandle: MTLSharedTextureHandle) -> (any MTLTexture)?
```

```objc
- (id<MTLTexture>) newSharedTextureWithHandle:(MTLSharedTextureHandle *) sharedHandle;
```

#### Return Value

A new [`MTLTexture`](../mtltexture.md) instance if the method completed successfully; otherwise `nil`.

#### Discussion

Call this method from the same [`MTLDevice`](../mtldevice.md) instance that created the shared texture instance.

> 💡 **Tip**:  You can identify the correct device with the texture handle’s [`device`](../mtlsharedtexturehandle/device.md) property.

## Parameters

- `sharedHandle`: An [`MTLSharedTextureHandle`](../mtlsharedtexturehandle.md) instance, typically from another process using the same GPU device.

## See Also

### Creating textures
- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](./maketexture%28descriptor%29.md)
  Creates a new texture instance.
- [func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?](./maketexture%28descriptor,iosurface,plane%29.md)
  Creates a texture instance that uses I/O surface to store its underlying data.
- [func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](./makesharedtexture%28descriptor%29.md)
  Creates a texture that you can share across process boundaries.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](./minimumlineartexturealignment%28for%29.md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [func minimumTextureBufferAlignment(for: MTLPixelFormat) -> Int](./minimumtexturebufferalignment%28for%29.md)
  Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makesharedtexture(handle:))*