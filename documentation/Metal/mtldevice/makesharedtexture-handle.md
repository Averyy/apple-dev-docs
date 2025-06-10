# makeSharedTexture(handle:)

**Framework**: Metal  
**Kind**: method  
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

#### Return Value

A new [`MTLTexture`](mtltexture.md) instance if the method completed successfully; otherwise `nil`.

#### Discussion

Call this method from the same [`MTLDevice`](mtldevice.md) instance that created the shared texture instance.

> 💡 **Tip**:  You can identify the correct device with the texture handle’s [`device`](mtlsharedtexturehandle/device.md) property.

## Parameters

- `sharedHandle`: An   instance, typically from another process using the same GPU device.

## See Also

- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/maketexture(descriptor:).md)
  Creates a new texture instance.
- [func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?](mtldevice/maketexture(descriptor:iosurface:plane:).md)
  Creates a texture instance that uses I/O surface to store its underlying data.
- [func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/makesharedtexture(descriptor:).md)
  Creates a texture that you can share across process boundaries.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](mtldevice/minimumlineartexturealignment(for:).md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [func minimumTextureBufferAlignment(for: MTLPixelFormat) -> Int](mtldevice/minimumtexturebufferalignment(for:).md)
  Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makesharedtexture(handle:))*