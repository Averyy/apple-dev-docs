# removeItem(_:named:from:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Removes an existing item from a given directory.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func removeItem(_ item: FSItem, named name: FSFileName, from directory: FSItem, context: FSContext) async throws -> FSRemoveItemResult
```

#### Discussion

Don’t actually remove the item object itself in your implementation; instead, only remove the given item name from the given directory. Remove and deallocate the item in [`reclaimItem(_:replyHandler:)`](fsvolume/handler/reclaimitem(_:replyhandler:).md).

## Parameters

- `item`: The item to remove.
- `name`: The name of the item to remove.
- `directory`: The directory from which to remove the item.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If removal succeeds, pass an instance of [`FSRemoveItemResult`](fsremoveitemresult.md) containing the [`FSItem.Attributes`](fsitem/attributes.md) of the removed item, the updated [`FSItem.Attributes`](fsitem/attributes.md) of the parent directory, and the volume’s updated free space, along with a `nil` error. If removal fails, pass the relevant error as the second parameter; FSKit ignores the [`FSRemoveItemResult`](fsremoveitemresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [func createItem(named: FSFileName, type: FSItem.ItemType, in: FSItem, attributes: FSItem.SetAttributesRequest, context: FSContext, replyHandler: (FSCreateItemResult?, (any Error)?) -> Void)](fsvolume/handler/createitem(named:type:in:attributes:context:replyhandler:).md)
  Creates a new file or directory item.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateItemResult](fscreateitemresult.md)
  The result of a create-item call.
- [func lookupItem(named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSLookupItemResult?, (any Error)?) -> Void)](fsvolume/handler/lookupitem(named:in:context:replyhandler:).md)
  Looks up an item within a directory.
- [class FSLookupItemResult](fslookupitemresult.md)
  The result of an item lookup call.
- [class FSRemoveItemResult](fsremoveitemresult.md)
  The result of a remove-item call.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, context: FSContext, replyHandler: (FSRenameItemResult?, (any Error)?) -> Void)](fsvolume/handler/renameitem(_:indirectory:named:to:indirectory:overitem:context:replyhandler:).md)
  Renames an item from one path in the file system to another.
- [class FSRenameItemResult](fsrenameitemresult.md)
  The result of a rename-item call.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/removeitem(_:named:from:context:replyhandler:))*