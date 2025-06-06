# MTLIOFileHandle

**Framework**: Metal  
**Kind**: protocol

Represents a raw or compressed file, such as a resource asset file in your app’s bundle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIOFileHandle : NSObjectProtocol
```

## Topics

### Naming a File Handle
- [var label: String?](mtliofilehandle/label.md)
  An optional name for the file that the handle represents.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLIOCommandBuffer](mtliocommandbuffer.md)
  A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [typealias MTLIOCommandBufferHandler](mtliocommandbufferhandler.md)
  A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [enum MTLIOStatus](mtliostatus.md)
  Represents the state of an input/output command buffer.
- [MTLIOError.Code](mtlioerror-swift.struct/code.md)
  The error codes for creating an input/output file handle.
- [let MTLIOErrorDomain: String](mtlioerrordomain.md)
  The domain for input/output command queue errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliofilehandle)*