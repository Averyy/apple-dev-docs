# remoteStorageTexture

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The texture on another GPU that the texture was created from, if any.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var remoteStorageTexture: (any MTLTexture)? { get }
```

#### Discussion

If the value of this property is non-`nil`, it contains a reference to the [`MTLTexture`](mtltexture.md) object that created this texture. If the texture isn’t a remote view, the value of this property is `nil`.

You can use remote views only as the source for copy commands encoded by a [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md).

## See Also

- [func makeRemoteTextureView(any MTLDevice) -> (any MTLTexture)?](mtltexture/makeremotetextureview(_:).md)
  Creates a remote texture view for another GPU in the same peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/remotestoragetexture)*