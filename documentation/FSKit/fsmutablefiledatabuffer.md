# FSMutableFileDataBuffer

**Framework**: FSKit  
**Kind**: class

A wrapper object for a data buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSMutableFileDataBuffer
```

#### Overview

This object provides a “zero-copy” buffer, for use when reading data from files. By not requiring additional buffer copying, this object reduces the extension’s memory footprint and improves performance. The `FSMutableFileDataBuffer` behaves similarly to a `uio` in the kernel.

## Topics

### Accessing buffer properties
- [func withUnsafeMutableBytes<R, E>((UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R](fsmutablefiledatabuffer/withunsafemutablebytes(_:).md)
  Performs the given closure with an unsafe pointer to the underlying bytes of the data buffer.
- [var length: Int](fsmutablefiledatabuffer/length.md)
  The data length of the buffer.
### Instance Methods
- [func createMutableRawSpan() throws -> MutableRawSpan](fsmutablefiledatabuffer/createmutablerawspan.md)
  Return a MutableRawSpan to the underlying bytes of the data buffer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func read(from: FSItem, at: off_t, length: Int, into: FSMutableFileDataBuffer, replyHandler: (FSReadFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/read(from:at:length:into:replyhandler:).md)
  Reads the contents of the given file item.
- [class FSReadFileResult](fsreadfileresult.md)
  The result of a read-file call.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (FSWriteFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/write(contents:to:at:replyhandler:).md)
  Writes contents to the given file item.
- [class FSWriteFileResult](fswritefileresult.md)
  The result of a read-file call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmutablefiledatabuffer)*