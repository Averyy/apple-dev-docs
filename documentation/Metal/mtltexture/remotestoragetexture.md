# remoteStorageTexture

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The texture on another GPU that the texture was created from, if any.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
var remoteStorageTexture: (any MTLTexture)? { get }
```

```objc
@property (readonly, nullable) id<MTLTexture> remoteStorageTexture;
```

#### Discussion

If the value of this property is non-`nil`, it contains a reference to the [`MTLTexture`](../mtltexture.md) instance that created this texture. If the texture isn’t a remote view, the value of this property is `nil`.

You can use remote views only as the source for copy commands encoded by an [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md).

## See Also

### Creating views of textures on other GPUs
- [func makeRemoteTextureView(any MTLDevice) -> (any MTLTexture)?](./makeremotetextureview%28_%29.md)
  Creates a remote texture view for another GPU in the same peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/remotestoragetexture)*