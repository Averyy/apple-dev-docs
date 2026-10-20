# readSymbolicLink(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Reads a symbolic link.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func readSymbolicLink(_ item: FSItem, replyHandler reply: @escaping @Sendable (FSFileName?, (any Error)?) -> Void)
```

```swift
func readSymbolicLink(_ item: FSItem) async throws -> FSFileName
```

```objc
- (void) readSymbolicLink:(FSItem *) item replyHandler:(void (^)(FSFileName *contents, NSError *error)) reply;
```

## Parameters

- `item`: The symbolic link to read from. FSKit guarantees this item is of type [`FSItem.ItemType.symlink`](../../fsitem/itemtype/symlink.md).
- `reply`: A block or closure to indicate success or failure. If reading succeeds, pass the link’s contents as an [`FSFileName`](../../fsfilename.md) and a `nil` error. If reading fails, pass the relevant error as the second parameter; FSKit ignores any [`FSFileName`](../../fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSFileName`](../../fsfilename.md) or throw an error.

## See Also

### Working with links
- [func createLink(to: FSItem, named: FSFileName, inDirectory: FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](./createlink%28to,named,indirectory,replyhandler%29.md)
  Creates a new hard link.
- [func createSymbolicLink(named: FSFileName, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./createsymboliclink%28named,indirectory,attributes,linkcontents,replyhandler%29.md)
  Creates a new symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/readsymboliclink(_:replyhandler:))*