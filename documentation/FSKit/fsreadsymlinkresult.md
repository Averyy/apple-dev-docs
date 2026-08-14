# FSReadSymlinkResult

**Framework**: FSKit  
**Kind**: class

The result of a read-symlink call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSReadSymlinkResult
```

#### Overview

Use this type in your implementation of [`readSymbolicLink(_:context:replyHandler:)`](fsvolume/handler/readsymboliclink(_:context:replyhandler:).md).

## Topics

### Creating a read-symlink result
- [init?(contents: FSFileName, symlinkAttributes: FSItem.Attributes)](fsreadsymlinkresult/init(contents:symlinkattributes:).md)
  Creates a result for a symlink-reading operation.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.

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

- [func createLink(to: FSItem, named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSCreateLinkResult?, (any Error)?) -> Void)](fsvolume/handler/createlink(to:named:in:context:replyhandler:).md)
  Creates a new hard link.
- [class FSCreateLinkResult](fscreatelinkresult.md)
  The result of a create-link call.
- [func createSymbolicLink(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, context: FSContext, replyHandler: (FSCreateSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/createsymboliclink(named:in:attributes:linkcontents:context:replyhandler:).md)
  Creates a new symbolic link.
- [class FSCreateSymlinkResult](fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/readsymboliclink(_:context:replyhandler:).md)
  Reads a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsreadsymlinkresult)*