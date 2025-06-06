# MTLIOStatus

**Framework**: Metal  
**Kind**: enum

Represents the state of an input/output command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLIOStatus
```

## Topics

### I/O Command Queue States
- [MTLIOStatus.pending](mtliostatus/pending.md)
  Indicates the GPU hasn’t finished executing the input/output command buffer.
- [MTLIOStatus.complete](mtliostatus/complete.md)
  Indicates the GPU has successfully finished executing the input/output command buffer.
- [MTLIOStatus.cancelled](mtliostatus/cancelled.md)
  Indicates the GPU has successfully abandoned the input/output command buffer.
- [MTLIOStatus.error](mtliostatus/error.md)
  Indicates the GPU experienced a problem with the input/output command buffer.
### Initializers
- [init?(rawValue: Int)](mtliostatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIOCommandBuffer](mtliocommandbuffer.md)
  A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [protocol MTLIOFileHandle](mtliofilehandle.md)
  Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [typealias MTLIOCommandBufferHandler](mtliocommandbufferhandler.md)
  A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [MTLIOError.Code](mtlioerror-swift.struct/code.md)
  The error codes for creating an input/output file handle.
- [let MTLIOErrorDomain: String](mtlioerrordomain.md)
  The domain for input/output command queue errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliostatus)*