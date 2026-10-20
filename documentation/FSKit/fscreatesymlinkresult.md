# FSCreateSymlinkResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a create-symlink call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSCreateSymlinkResult
```

```objc
@interface FSCreateSymlinkResult : FSCreateItemResult
```

#### Overview

Use this type in your implementation of  [`createSymbolicLink(named:in:attributes:linkContents:context:replyHandler:)`](./fsvolume/handler/createsymboliclink%28named,in,attributes,linkcontents,context,replyhandler%29.md).

## Relationships

### Inherits From
- [FSCreateItemResult](./fscreateitemresult.md)
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
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](./fsvolume/handler/readsymboliclink%28_,context,replyhandler%29.md)
  Reads a symbolic link.
- [class FSReadSymlinkResult](./fsreadsymlinkresult.md)
  The result of a read-symlink call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreatesymlinkresult)*