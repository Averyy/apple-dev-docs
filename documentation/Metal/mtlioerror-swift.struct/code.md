# MTLIOError.Code

**Framework**: Metal  
**Kind**: enum

The error codes for creating an input/output file handle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
- [MTLIOError.Code.urlInvalid](mtlioerror-swift.struct/code/urlinvalid.md)
  An error code that represents a problem with a file URL.
- [MTLIOError.Code.internal](mtlioerror-swift.struct/code/internal.md)
  An error code that represents a problem internal to the Metal framework.
- [MTLIOError.Code.urlInvalid](mtlioerror-swift.struct/code/urlinvalid.md)
  An error code that represents a problem with a file URL.
- [MTLIOError.Code.internal](mtlioerror-swift.struct/code/internal.md)
  An error code that represents a problem internal to the Metal framework.
### Initializers
- [init?(rawValue: Int)](mtlioerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTLIOCommandBuffer](mtliocommandbuffer.md)
  A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [protocol MTLIOFileHandle](mtliofilehandle.md)
  Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [typealias MTLIOCommandBufferHandler](mtliocommandbufferhandler.md)
  A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [enum MTLIOStatus](mtliostatus.md)
  Represents the state of an input/output command buffer.
- [let MTLIOErrorDomain: String](mtlioerrordomain.md)
  The domain for input/output command queue errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlioerror-swift.struct/code)*