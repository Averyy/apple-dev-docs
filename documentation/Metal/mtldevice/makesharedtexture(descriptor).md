# makeSharedTexture(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a texture that you can share across process boundaries.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?
```

```objc
- (id<MTLTexture>) newSharedTextureWithDescriptor:(MTLTextureDescriptor *) descriptor;
```

#### Return Value

A new [`MTLTexture`](../mtltexture.md) instance if the method completed successfully; otherwise `nil`.

#### Discussion

You can create a shared texture but only with [`storageModePrivate`](../mtlresourceoptions/storagemodeprivate.md). You can share the texture with another process by:

1. Creating a texture handle (see [`makeSharedTextureHandle()`](../mtltexture/makesharedtexturehandle%28%29.md))
2. Passing the texture handle to the other process
3. Creating a texture in the other process by calling the [`makeSharedTexture(handle:)`](./makesharedtexture%28handle%29.md)method

> ❗ **Important**:  You can share a texture with another process that uses the same GPU, but not with a different GPU.

## Parameters

- `descriptor`: An [`MTLTextureDescriptor`](../mtltexturedescriptor.md) instance.

## See Also

### Creating textures
- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](./maketexture%28descriptor%29.md)
  Creates a new texture instance.
- [func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?](./maketexture%28descriptor,iosurface,plane%29.md)
  Creates a texture instance that uses I/O surface to store its underlying data.
- [func makeSharedTexture(handle: MTLSharedTextureHandle) -> (any MTLTexture)?](./makesharedtexture%28handle%29.md)
  Creates a texture that references a shared texture.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](./minimumlineartexturealignment%28for%29.md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [func minimumTextureBufferAlignment(for: MTLPixelFormat) -> Int](./minimumtexturebufferalignment%28for%29.md)
  Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makesharedtexture(descriptor:))*