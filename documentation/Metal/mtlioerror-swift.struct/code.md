# MTLIOError.Code

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MTLIOError : NSInteger;
```

## Topics

### Error codes
- [MTLIOError.Code.urlInvalid](./code/urlinvalid.md)
  An error code that represents a problem with a file URL.
- [MTLIOError.Code.internal](./code/internal.md)
  An error code that represents a problem internal to the Metal framework.
- [MTLIOError.Code.urlInvalid](./code/urlinvalid.md)
  An error code that represents a problem with a file URL.
- [MTLIOError.Code.internal](./code/internal.md)
  An error code that represents a problem internal to the Metal framework.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### I/O command buffers
- [protocol MTLIOCommandBuffer](../mtliocommandbuffer.md)
  A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [protocol MTLIOFileHandle](../mtliofilehandle.md)
  Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [typealias MTLIOCommandBufferHandler](../mtliocommandbufferhandler.md)
  A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [enum MTLIOStatus](../mtliostatus.md)
  Represents the state of an input/output command buffer.
- [let MTLIOErrorDomain: String](../mtlioerrordomain.md)
  The domain for input/output command queue errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlioerror-swift.struct/code)*