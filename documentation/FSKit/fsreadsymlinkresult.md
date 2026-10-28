# FSReadSymlinkResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a read-symlink call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSReadSymlinkResult
```

```objc
@interface FSReadSymlinkResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`readSymbolicLink(_:context:replyHandler:)`](./fsvolume/handler/readsymboliclink%28_,context,replyhandler%29.md).

## Topics

### Creating a read-symlink result
- [init?(contents: FSFileName, symlinkAttributes: FSItem.Attributes)](./fsreadsymlinkresult/init%28contents,symlinkattributes%29.md)
  Creates a result for a symlink-reading operation.
- [class FSFileName](./fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.

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

### Working with links
- [func createLink(to: FSItem, named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSCreateLinkResult?, (any Error)?) -> Void)](./fsvolume/handler/createlink%28to,named,in,context,replyhandler%29.md)
  Creates a new hard link.
- [class FSCreateLinkResult](./fscreatelinkresult.md)
  The result of a create-link call.
- [func createSymbolicLink(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, context: FSContext, replyHandler: (FSCreateSymlinkResult?, (any Error)?) -> Void)](./fsvolume/handler/createsymboliclink%28named,in,attributes,linkcontents,context,replyhandler%29.md)
  Creates a new symbolic link.
- [class FSCreateSymlinkResult](./fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](./fsvolume/handler/readsymboliclink%28_,context,replyhandler%29.md)
  Reads a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsreadsymlinkresult)*