# makeRemoteTextureView(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a remote texture view for another GPU in the same peer group.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func makeRemoteTextureView(_ device: any MTLDevice) -> (any MTLTexture)?
```

## Mentions

- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)

#### Discussion

The device object that created this texture, and the device object passed into this method, must have the same nonzero peer group identifier ([`peerGroupID`](mtldevice/peergroupid.md)). This texture must either use the private storage mode ([`MTLStorageMode.private`](mtlstoragemode/private.md)) or be backed by an [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface).

A remote view doesn’t allocate any storage for the new texture; it references the memory allocated for the original texture. You can use remote views only as a source for copy commands encoded by a [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md). For more information, see [`Transferring Data Between Connected GPUs`](transferring-data-between-connected-gpus.md).

## See Also

- [var remoteStorageTexture: (any MTLTexture)?](mtltexture/remotestoragetexture.md)
  The texture on another GPU that the texture was created from, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/makeremotetextureview(_:))*