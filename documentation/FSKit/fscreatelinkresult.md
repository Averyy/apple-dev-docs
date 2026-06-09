# FSCreateLinkResult

**Framework**: FSKit  
**Kind**: class

The result of a create-link call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSCreateLinkResult
```

#### Overview

Use this type in your implementation of [`createLink(to:named:in:context:replyHandler:)`](fsvolume/handler/createlink(to:named:in:context:replyhandler:).md).

## Topics

### Creating a create-link result
- [init?(linkName: FSFileName, linkAttributes: FSItem.Attributes, directoryAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](fscreatelinkresult/init(linkname:linkattributes:directoryattributes:freespace:).md)
  Creates a result for a link-creation operation.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

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

- [func createLink(to: FSItem, named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSCreateLinkResult?, (any Error)?) -> Void)](fsvolume/handler/createlink(to:named:in:context:replyhandler:).md)
  Creates a new hard link.
- [func createSymbolicLink(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, context: FSContext, replyHandler: (FSCreateSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/createsymboliclink(named:in:attributes:linkcontents:context:replyhandler:).md)
  Creates a new symbolic link.
- [class FSCreateSymlinkResult](fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/readsymboliclink(_:context:replyhandler:).md)
  Reads a symbolic link.
- [class FSReadSymlinkResult](fsreadsymlinkresult.md)
  The result of a read-symlink call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreatelinkresult)*