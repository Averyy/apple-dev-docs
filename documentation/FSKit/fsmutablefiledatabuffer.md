# FSMutableFileDataBuffer

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A wrapper object for a data buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSMutableFileDataBuffer
```

```objc
@interface FSMutableFileDataBuffer : NSObject
```

## Overview

This object provides a “zero-copy” buffer, for use when reading data from files. By not requiring additional buffer copying, this object reduces the extension’s memory footprint and improves performance. The `FSMutableFileDataBuffer` behaves similarly to a `uio` in the kernel.

## Topics

### Accessing buffer properties
- [func withUnsafeMutableBytes<R, E>((UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R](./fsmutablefiledatabuffer/withunsafemutablebytes%28_%29.md)
  Performs the given closure with an unsafe pointer to the underlying bytes of the data buffer.
- [var length: Int](./fsmutablefiledatabuffer/length.md)
  The data length of the buffer.
- [- mutableBytes](./fsmutablefiledatabuffer/mutablebytes.md)
  The byte data.
### Instance Methods
- [func createMutableRawSpan() throws -> MutableRawSpan](./fsmutablefiledatabuffer/createmutablerawspan%28%29.md)
  Return a MutableRawSpan to the underlying bytes of the data buffer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Reading and writing
- [func read(from: FSItem, at: off_t, length: Int, into: FSMutableFileDataBuffer, replyHandler: (FSReadFileResult?, (any Error)?) -> Void)](./fsvolume/readwritehandler/read%28from,at,length,into,replyhandler%29.md)
  Reads the contents of the given file item.
- [class FSReadFileResult](./fsreadfileresult.md)
  The result of a read-file call.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (FSWriteFileResult?, (any Error)?) -> Void)](./fsvolume/readwritehandler/write%28contents,to,at,replyhandler%29.md)
  Writes contents to the given file item.
- [class FSWriteFileResult](./fswritefileresult.md)
  The result of a read-file call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmutablefiledatabuffer)*