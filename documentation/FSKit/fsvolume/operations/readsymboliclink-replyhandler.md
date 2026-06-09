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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/readsymboliclink(_:replyhandler:))*