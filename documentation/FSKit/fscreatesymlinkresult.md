# FSCreateSymlinkResult

**Framework**: FSKit  
**Kind**: class

The result of a create-symlink call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSCreateSymlinkResult
```

#### Overview

Use this type in your implementation of  [`createSymbolicLink(named:in:attributes:linkContents:context:replyHandler:)`](fsvolume/handler/createsymboliclink(named:in:attributes:linkcontents:context:replyhandler:).md).

## Relationships

### Inherits From
- [FSCreateItemResult](fscreateitemresult.md)
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
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/readsymboliclink(_:context:replyhandler:).md)
  Reads a symbolic link.
- [class FSReadSymlinkResult](fsreadsymlinkresult.md)
  The result of a read-symlink call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreatesymlinkresult)*