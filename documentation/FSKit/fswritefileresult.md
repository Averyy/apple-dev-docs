# FSWriteFileResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a read-file call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSWriteFileResult
```

```objc
@interface FSWriteFileResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of [`write(contents:to:at:replyHandler:)`](./fsvolume/readwritehandler/write%28contents,to,at,replyhandler%29.md).

## Topics

### Creating a write-file result
- [init?(bytesWritten: Int, itemAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](./fswritefileresult/init%28byteswritten,itemattributes,freespace%29.md)
  Creates a result for a file-writing operation.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](./fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
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
- [class FSMutableFileDataBuffer](./fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [class FSReadFileResult](./fsreadfileresult.md)
  The result of a read-file call.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (FSWriteFileResult?, (any Error)?) -> Void)](./fsvolume/readwritehandler/write%28contents,to,at,replyhandler%29.md)
  Writes contents to the given file item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fswritefileresult)*