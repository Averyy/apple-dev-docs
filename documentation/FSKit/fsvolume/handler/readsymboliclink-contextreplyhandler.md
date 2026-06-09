# readSymbolicLink(_:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Reads a symbolic link.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func readSymbolicLink(_ item: FSItem, context: FSContext) async throws -> FSReadSymlinkResult
```

## Parameters

- `item`: The symbolic link to read from. FSKit guarantees this item is of type [`FSItem.ItemType.symlink`](fsitem/itemtype/symlink.md).
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If reading succeeds, pass an instance of [`FSReadSymlinkResult`](fsreadsymlinkresult.md) containing the link’s contents and attributes, along with a `nil` error. If reading fails, pass the relevant error as the second parameter; FSKit ignores the [`FSReadSymlinkResult`](fsreadsymlinkresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [func createLink(to: FSItem, named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSCreateLinkResult?, (any Error)?) -> Void)](fsvolume/handler/createlink(to:named:in:context:replyhandler:).md)
  Creates a new hard link.
- [class FSCreateLinkResult](fscreatelinkresult.md)
  The result of a create-link call.
- [func createSymbolicLink(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, context: FSContext, replyHandler: (FSCreateSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/createsymboliclink(named:in:attributes:linkcontents:context:replyhandler:).md)
  Creates a new symbolic link.
- [class FSCreateSymlinkResult](fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [class FSReadSymlinkResult](fsreadsymlinkresult.md)
  The result of a read-symlink call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/readsymboliclink(_:context:replyhandler:))*