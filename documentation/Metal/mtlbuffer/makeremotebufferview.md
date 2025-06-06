# makeRemoteBufferView(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a remote view of the buffer for another GPU in the same peer group.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func makeRemoteBufferView(_ device: any MTLDevice) -> (any MTLBuffer)?
```

## Mentions

- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)

#### Discussion

The device object that created this buffer, and the device object passed into this method, must have the same nonzero peer group identifier ([`peerGroupID`](mtldevice/peergroupid.md)). This buffer must use the private storage mode ([`MTLStorageMode.private`](mtlstoragemode/private.md)).

A remote view doesn’t allocate any storage for the new buffer; it references the memory allocated for the original buffer. You can use remote views only as a source for copy commands encoded by a [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md). For more information, see [`Transferring Data Between Connected GPUs`](transferring-data-between-connected-gpus.md).

## See Also

- [var remoteStorageBuffer: (any MTLBuffer)?](mtlbuffer/remotestoragebuffer.md)
  The buffer on another GPU that the buffer was created from, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/makeremotebufferview(_:))*