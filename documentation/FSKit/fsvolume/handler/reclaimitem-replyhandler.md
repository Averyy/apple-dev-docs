# reclaimItem(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Reclaims an item, releasing any resources allocated for the item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func reclaimItem(_ item: FSItem) async throws
```

#### Discussion

`::::: Swift ::::::::::`

- reply: A block or closure to indicate success or failure. If removal fails, pass an error as the one parameter to the reply handler. If removal succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

`::::::::::::::::::::`

`::::: ObjC ::::::::::`

- error: A block or closure to indicate success or failure. If removal fails, pass an error as the one parameter to the reply handler. If removal succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

`::::::::::::::::::::`

#### Discussion

FSKit guarantees that for every [`FSItem`](fsitem.md) returned by the volume, a corresponding reclaim operation occurs after the upper layers no longer reference that item. To use this behavior, call [`tryReclaim(_:)`](fsitem/tryreclaim(_:).md) in your implementation of this method.

> **Note**:  Block device file systems may assess whether an underlying resource terminates before processing reclaim operations. On unary file systems, for example, the associated volumes unmount when such resources disconnect from the system. The unmount triggers a reclaiming of all items. Some implementations benefit greatly from short-circuiting in such cases. With a terminated resource, all I/O results in an error, making short-circuiting the most efficient response.

## Parameters

- `item`: The item to reclaim.

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
- [func removeItem(FSItem, named: FSFileName, from: FSItem, context: FSContext, replyHandler: (FSRemoveItemResult?, (any Error)?) -> Void)](fsvolume/handler/removeitem(_:named:from:context:replyhandler:).md)
  Removes an existing item from a given directory.
- [class FSRemoveItemResult](fsremoveitemresult.md)
  The result of a remove-item call.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, context: FSContext, replyHandler: (FSRenameItemResult?, (any Error)?) -> Void)](fsvolume/handler/renameitem(_:indirectory:named:to:indirectory:overitem:context:replyhandler:).md)
  Renames an item from one path in the file system to another.
- [class FSRenameItemResult](fsrenameitemresult.md)
  The result of a rename-item call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/reclaimitem(_:replyhandler:))*