# makeTexture(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new texture instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?
```

```objc
- (id<MTLTexture>) newTextureWithDescriptor:(MTLTextureDescriptor *) descriptor;
```

## Mentions

- [Setting resource storage modes](../setting-resource-storage-modes.md)

## Return Value

A new [`MTLTexture`](../mtltexture.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `descriptor`: An [`MTLTextureDescriptor`](../mtltexturedescriptor.md) instance.

## See Also

### Creating textures
- [func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?](./maketexture%28descriptor,iosurface,plane%29.md)
  Creates a texture instance that uses I/O surface to store its underlying data.
- [func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](./makesharedtexture%28descriptor%29.md)
  Creates a texture that you can share across process boundaries.
- [func makeSharedTexture(handle: MTLSharedTextureHandle) -> (any MTLTexture)?](./makesharedtexture%28handle%29.md)
  Creates a texture that references a shared texture.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](./minimumlineartexturealignment%28for%29.md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [func minimumTextureBufferAlignment(for: MTLPixelFormat) -> Int](./minimumtexturebufferalignment%28for%29.md)
  Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maketexture(descriptor:))*