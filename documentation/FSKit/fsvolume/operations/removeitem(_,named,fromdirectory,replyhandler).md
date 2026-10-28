# removeItem(_:named:fromDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes an existing item from a given directory.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func removeItem(_ item: FSItem, named name: FSFileName, fromDirectory directory: FSItem, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeItem(_ item: FSItem, named name: FSFileName, fromDirectory directory: FSItem) async throws
```

```objc
- (void) removeItem:(FSItem *) item named:(FSFileName *) name fromDirectory:(FSItem *) directory replyHandler:(void (^)(NSError *error)) reply;
```

## Discussion

Don’t actually remove the item object itself in your implementation; instead, only remove the given item name from the given directory. Remove and deallocate the item in `reclaimItem(_:)`.

## Parameters

- `item`: The item to remove.
- `name`: The name of the item to remove.
- `directory`: The directory from which to remove the item.
- `reply`: A block or closure to indicate success or failure. If removal fails, pass an error as the one parameter to the reply handler. If removal succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

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
- [func lookupItem(named: FSFileName, inDirectory: FSItem, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./lookupitem%28named,indirectory,replyhandler%29.md)
  Looks up an item within a directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](./renameitem%28_,indirectory,named,to,indirectory,overitem,replyhandler%29.md)
  Renames an item from one path in the file system to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/removeitem(_:named:fromdirectory:replyhandler:))*