# FSWriteFileResult

**Framework**: FSKit  
**Kind**: class

The result of a read-file call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSWriteFileResult
```

#### Overview

Use this type in your implementation of [`write(contents:to:at:replyHandler:)`](fsvolume/readwritehandler/write(contents:to:at:replyhandler:).md).

## Topics

### Creating a write-file result
- [init?(bytesWritten: Int, itemAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](fswritefileresult/init(byteswritten:itemattributes:freespace:).md)
  Creates a result for a file-writing operation.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func read(from: FSItem, at: off_t, length: Int, into: FSMutableFileDataBuffer, replyHandler: (FSReadFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/read(from:at:length:into:replyhandler:).md)
  Reads the contents of the given file item.
- [class FSMutableFileDataBuffer](fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [class FSReadFileResult](fsreadfileresult.md)
  The result of a read-file call.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (FSWriteFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/write(contents:to:at:replyhandler:).md)
  Writes contents to the given file item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fswritefileresult)*