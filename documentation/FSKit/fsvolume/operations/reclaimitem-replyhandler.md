# reclaimItem(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Reclaims an item, releasing any resources allocated for the item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func reclaimItem(_ item: FSItem) async throws
```

#### Discussion

FSKit guarantees that for every [`FSItem`](fsitem.md) returned by the volume, a corresponding reclaim operation occurs after the upper layers no longer reference that item.

> **Note**: Block device file systems may assess whether an underyling resource terminates before processing reclaim operations. On unary file systems, for example, the associated volumes unmount when such resources disconnect from the system. The unmount triggers a reclaiming of all items. Some implementations benefit greatly from short-circuiting in such cases. With a terminated resource, all I/O results in an error, making short-circuiting the most efficient response.

Block device file systems may assess whether an underyling resource terminates before processing reclaim operations. On unary file systems, for example, the associated volumes unmount when such resources disconnect from the system. The unmount triggers a reclaiming of all items. Some implementations benefit greatly from short-circuiting in such cases. With a terminated resource, all I/O results in an error, making short-circuiting the most efficient response.

## Parameters

- `item`: The item to reclaim.
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
- [func removeItem(FSItem, named: FSFileName, fromDirectory: FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/removeitem(_:named:fromdirectory:replyhandler:).md)
  Removes an existing item from a given directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/renameitem(_:indirectory:named:to:indirectory:overitem:replyhandler:).md)
  Renames an item from one path in the file system to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/reclaimitem(_:replyhandler:))*