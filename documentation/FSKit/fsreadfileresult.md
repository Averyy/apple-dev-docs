# FSReadFileResult

**Framework**: FSKit  
**Kind**: class

The result of a read-file call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSReadFileResult
```

#### Overview

Use this type in your implementation of [`read(from:at:length:into:replyHandler:)`](fsvolume/readwritehandler/read(from:at:length:into:replyhandler:).md).

## Topics

### Creating a read-file result
- [init?(bytesRead: Int, itemAttributes: FSItem.Attributes)](fsreadfileresult/init(bytesread:itemattributes:).md)
  Creates a result for a file-reading operation.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
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
- [class FSMutableFileDataBuffer](fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (FSWriteFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/write(contents:to:at:replyhandler:).md)
  Writes contents to the given file item.
- [class FSWriteFileResult](fswritefileresult.md)
  The result of a read-file call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsreadfileresult)*