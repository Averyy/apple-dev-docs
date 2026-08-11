# createItem(named:type:in:attributes:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new file or directory item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func createItem(named name: FSFileName, type: FSItem.ItemType, in directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, context: FSContext) async throws -> FSCreateItemResult
```

#### Discussion

If an item named `name` already exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and a code of `EEXIST`.

## Parameters

- `name`: The new item’s name.
- `type`: The new item’s type.  Valid values are [`FSItem.ItemType.file`](fsitem/itemtype/file.md) or [`FSItem.ItemType.directory`](fsitem/itemtype/directory.md).
- `directory`: The directory in which to create the item.
- `newAttributes`: Attributes to apply to the new item.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass an instance of [`FSCreateItemResult`](fscreateitemresult.md) containing the newly-created [`FSItem`](fsitem.md), its [`FSFileName`](fsfilename.md), its [`FSItem.Attributes`](fsitem/attributes.md), the updated [`FSItem.Attributes`](fsitem/attributes.md) of the parent directory, and the volume’s updated free space, along with a `nil` error. If creation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSCreateItemResult`](fscreateitemresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

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
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/reclaimitem(_:replyhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/createitem(named:type:in:attributes:context:replyhandler:))*