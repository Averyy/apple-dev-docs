# lookupItem(named:inDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Looks up an item within a directory.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func lookupItem(named name: FSFileName, inDirectory directory: FSItem, replyHandler reply: @escaping @Sendable (FSItem?, FSFileName?, (any Error)?) -> Void)
```

```swift
func lookupItem(named name: FSFileName, inDirectory directory: FSItem) async throws -> (FSItem, FSFileName)
```

```objc
- (void) lookupItemNamed:(FSFileName *) name inDirectory:(FSItem *) directory replyHandler:(void (^)(FSItem *theItem, FSFileName *itemName, NSError *error)) reply;
```

## Discussion

If no item matching `name` exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](../../../Foundation/nsposixerrordomain.md) and a code of `ENOENT`.

> 💡 **Tip**: The [`FSFileName`](../../fsfilename.md) sent back to the caller may differ from the `name` parameter. This flexibility allows your implementation to handle case-insensitive and case-sensitive file systems. It might also be the case that `name` uses a composed Unicode string, but the name maintained by the file system and provided to the caller is uncomposed Unicode.

## Parameters

- `name`: The name of the item to look up.
- `directory`: The directory in which to look up the item.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass the found [`FSItem`](../../fsitem.md) and its [`FSFileName`](../../fsfilename.md) (as saved within the file system), along with a `nil` error. If lookup fails, pass the relevant error as the third parameter; any [`FSItem`](../../fsitem.md) or [`FSFileName`](../../fsfilename.md) are ignored in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSItem`](../../fsitem.md) and [`FSFileName`](../../fsfilename.md) as a tuple or throw an error.

## See Also

### Working with items
- [func createItem(named: FSFileName, type: FSItem.ItemType, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./createitem%28named,type,indirectory,attributes,replyhandler%29.md)
  Creates a new file or directory item.
- [class FSFileName](../../fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](../../fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](../../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func removeItem(FSItem, named: FSFileName, fromDirectory: FSItem, replyHandler: ((any Error)?) -> Void)](./removeitem%28_,named,fromdirectory,replyhandler%29.md)
  Removes an existing item from a given directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](./renameitem%28_,indirectory,named,to,indirectory,overitem,replyhandler%29.md)
  Renames an item from one path in the file system to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/lookupitem(named:indirectory:replyhandler:))*