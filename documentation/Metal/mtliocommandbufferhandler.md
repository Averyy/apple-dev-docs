# MTLIOCommandBufferHandler

**Framework**: Metal  
**Kind**: typealias

A convenience type that defines the signature of an input/output command buffer’s completion handler.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLIOCommandBufferHandler = (any MTLIOCommandBuffer) -> Void
```

## Parameters

- `inputOutputCommandBuffer`: The   instance that has finished executing is calling your completion handler.

## See Also

- [protocol MTLIOCommandBuffer](mtliocommandbuffer.md)
  A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [protocol MTLIOFileHandle](mtliofilehandle.md)
  Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [enum MTLIOStatus](mtliostatus.md)
  Represents the state of an input/output command buffer.
- [MTLIOError.Code](mtlioerror-swift.struct/code.md)
  The error codes for creating an input/output file handle.
- [let MTLIOErrorDomain: String](mtlioerrordomain.md)
  The domain for input/output command queue errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbufferhandler)*