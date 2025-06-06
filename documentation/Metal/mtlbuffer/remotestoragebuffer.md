# remoteStorageBuffer

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The buffer on another GPU that the buffer was created from, if any.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var remoteStorageBuffer: (any MTLBuffer)? { get }
```

#### Discussion

If the value of this property is non-`nil`, it contains a reference to the [`MTLBuffer`](mtlbuffer.md) object that created this buffer. If the buffer isn’t a remote view, the value of this property is `nil`.

You can use remote views only as a source for copy commands encoded by a [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md).

## See Also

- [func makeRemoteBufferView(any MTLDevice) -> (any MTLBuffer)?](mtlbuffer/makeremotebufferview(_:).md)
  Creates a remote view of the buffer for another GPU in the same peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/remotestoragebuffer)*