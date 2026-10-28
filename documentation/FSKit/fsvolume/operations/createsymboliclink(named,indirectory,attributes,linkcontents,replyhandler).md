# createSymbolicLink(named:inDirectory:attributes:linkContents:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new symbolic link.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func createSymbolicLink(named name: FSFileName, inDirectory directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, linkContents contents: FSFileName, replyHandler reply: @escaping @Sendable (FSItem?, FSFileName?, (any Error)?) -> Void)
```

```swift
func createSymbolicLink(named name: FSFileName, inDirectory directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, linkContents contents: FSFileName) async throws -> (FSItem, FSFileName)
```

```objc
- (void) createSymbolicLinkNamed:(FSFileName *) name inDirectory:(FSItem *) directory attributes:(FSItemSetAttributesRequest *) newAttributes linkContents:(FSFileName *) contents replyHandler:(void (^)(FSItem *newItem, FSFileName *newItemName, NSError *error)) reply;
```

## Discussion

If an item named `name` already exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](../../../Foundation/nsposixerrordomain.md) and a code of `EEXIST`.

## Parameters

- `name`: The new item’s name.
- `directory`: The directory in which to create the item.
- `newAttributes`: Attributes to apply to the new item.
- `contents`: The contents of the new symbolic link.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass the newly-created [`FSItem`](../../fsitem.md) and a `nil` error. If creation fails, pass the relevant error as the second parameter; FSKit ignores any [`FSItem`](../../fsitem.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSItem`](../../fsitem.md) or throw an error.

## See Also

### Working with links
- [func createLink(to: FSItem, named: FSFileName, inDirectory: FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](./createlink%28to,named,indirectory,replyhandler%29.md)
  Creates a new hard link.
- [func readSymbolicLink(FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](./readsymboliclink%28_,replyhandler%29.md)
  Reads a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/createsymboliclink(named:indirectory:attributes:linkcontents:replyhandler:))*