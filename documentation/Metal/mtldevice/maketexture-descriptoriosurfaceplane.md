# makeTexture(descriptor:iosurface:plane:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a texture instance that uses I/O surface to store its underlying data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?
```

#### Return Value

A new [`MTLTexture`](mtltexture.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `descriptor`: An   instance.
- `iosurface`: An   instance.
- `plane`: A plane within i  the method sets as the texture’s underlying data.

## See Also

- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/maketexture(descriptor:).md)
  Creates a new texture instance.
- [func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/makesharedtexture(descriptor:).md)
  Creates a texture that you can share across process boundaries.
- [func makeSharedTexture(handle: MTLSharedTextureHandle) -> (any MTLTexture)?](mtldevice/makesharedtexture(handle:).md)
  Creates a texture that references a shared texture.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](mtldevice/minimumlineartexturealignment(for:).md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [func minimumTextureBufferAlignment(for: MTLPixelFormat) -> Int](mtldevice/minimumtexturebufferalignment(for:).md)
  Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maketexture(descriptor:iosurface:plane:))*