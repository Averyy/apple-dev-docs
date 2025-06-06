# removeItem(_:named:fromDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Removes an existing item from a given directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func removeItem(_ item: FSItem, named name: FSFileName, fromDirectory directory: FSItem) async throws
```

#### Discussion

Don’t actually remove the item object itself in your implementation; instead, only remove the given item name from the given directory. Remove and deallocate the item in [`reclaimItem(_:replyHandler:)`](fsvolume/operations/reclaimitem(_:replyhandler:).md).

## Parameters

- `item`: The item to remove.
- `name`: The name of the item to remove.
- `directory`: The directory from which to remove the item.
- `reply`: A block or closure to indicate success or failure. If removal fails, pass an error as the one parameter to the reply handler. If removal succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

- [func createItem(named: FSFileName, type: FSItem.ItemType, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createitem(named:type:indirectory:attributes:replyhandler:).md)
  Creates a new file or directory item.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(named: FSFileName, inDirectory: FSItem, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolume/operations/lookupitem(named:indirectory:replyhandler:).md)
  Looks up an item within a directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/renameitem(_:indirectory:named:to:indirectory:overitem:replyhandler:).md)
  Renames an item from one path in the file system to another.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/removeitem(_:named:fromdirectory:replyhandler:))*