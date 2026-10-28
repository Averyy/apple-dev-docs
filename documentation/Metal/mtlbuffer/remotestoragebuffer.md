# remoteStorageBuffer

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The buffer on another GPU that the buffer was created from, if any.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
var remoteStorageBuffer: (any MTLBuffer)? { get }
```

```objc
@property (readonly, nullable) id<MTLBuffer> remoteStorageBuffer;
```

## Discussion

If the value of this property is non-`nil`, it contains a reference to the [`MTLBuffer`](../mtlbuffer.md) instance that created this buffer. If the buffer isn’t a remote view, the value of this property is `nil`.

You can use remote views only as a source for copy commands encoded by an [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md).

## See Also

### Creating views of buffers on other GPUs
- [func makeRemoteBufferView(any MTLDevice) -> (any MTLBuffer)?](./makeremotebufferview%28_%29.md)
  Creates a remote view of the buffer for another GPU in the same peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/remotestoragebuffer)*