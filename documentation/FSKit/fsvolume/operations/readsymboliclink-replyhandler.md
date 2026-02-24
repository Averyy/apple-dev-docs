# readSymbolicLink(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Reads a symbolic link.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func readSymbolicLink(_ item: FSItem) async throws -> FSFileName
```

## Parameters

- `item`: The symbolic link to read from. FSKit guarantees this item is of type [`FSItem.ItemType.symlink`](fsitem/itemtype/symlink.md).
- `reply`: A block or closure to indicate success or failure. If reading succeeds, pass the link’s contents as an [`FSFileName`](fsfilename.md) and a `nil` error. If reading fails, pass the relevant error as the second parameter; FSKit ignores any [`FSFileName`](fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSFileName`](fsfilename.md) or throw an error.

## See Also

- [func createLink(to: FSItem, named: FSFileName, inDirectory: FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createlink(to:named:indirectory:replyhandler:).md)
  Creates a new hard link.
- [func createSymbolicLink(named: FSFileName, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createsymboliclink(named:indirectory:attributes:linkcontents:replyhandler:).md)
  Creates a new symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/readsymboliclink(_:replyhandler:))*