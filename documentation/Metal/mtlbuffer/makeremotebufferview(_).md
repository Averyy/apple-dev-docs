# makeRemoteBufferView(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a remote view of the buffer for another GPU in the same peer group.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
func makeRemoteBufferView(_ device: any MTLDevice) -> (any MTLBuffer)?
```

```objc
- (id<MTLBuffer>) newRemoteBufferViewForDevice:(id<MTLDevice>) device;
```

## Mentions

- [Transferring data between connected GPUs](../transferring-data-between-connected-gpus.md)

## Discussion

The device instance that this buffer belongs to and the device you pass to the method both need to have the same nonzero peer group identifier ([`peerGroupID`](../mtldevice/peergroupid.md)). This buffer needs to use the private storage mode ([`MTLStorageMode.private`](../mtlstoragemode/private.md)).

A remote view doesn’t allocate any storage for the new buffer; it references the memory allocated for the original buffer. You can use remote views only as a source for copy commands encoded by an [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md). For more information, see [Transferring data between connected GPUs](../transferring-data-between-connected-gpus.md).

## See Also

### Creating views of buffers on other GPUs
- [var remoteStorageBuffer: (any MTLBuffer)?](./remotestoragebuffer.md)
  The buffer on another GPU that the buffer was created from, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/makeremotebufferview(_:))*