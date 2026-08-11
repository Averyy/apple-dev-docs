# reclaimItem(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func reclaimItem(_ item: FSItem) async throws
```

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