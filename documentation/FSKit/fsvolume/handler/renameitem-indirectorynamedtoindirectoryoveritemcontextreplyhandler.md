# renameItem(_:inDirectory:named:to:inDirectory:overItem:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Renames an item from one path in the file system to another.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func renameItem(_ item: FSItem, inDirectory sourceDirectory: FSItem, named sourceName: FSFileName, to destinationName: FSFileName, inDirectory destinationDirectory: FSItem, overItem: FSItem?, context: FSContext) async throws -> FSRenameItemResult
```

#### Discussion

Implement renaming along the lines of this algorithm:

- If `item` is a file: - If the destination file exists: - Remove the destination file.
- If the source and destination directories are the same: - Rewrite the name in the existing directory.
- Else: - Write the new entry in the destination directory.
- Clear the old directory entry.
- If `item` is a directory: - If the destination directory exists: - If the destination directory isn’t empty: - Fail the operation with an error of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and a code of `ENOTEMPTY`.
- Else: - Remove the destination directory.
- If the source and destination directories are the same: - Rewrite the name in the existing directory.
- Else: - If the destination is a child of the source directory: - Fail the operation with an error.
- Else: - Write the new entry in the destination directory.
- Update `"."` and `".."` in the moved directory.
- Clear the old directory entry.

## Parameters

- `item`: The file system object being renamed.
- `sourceDirectory`: The directory that currently contains the item to rename.
- `sourceName`: The name of the item within the source directory.
- `destinationName`: The new name of the item as it appears in `destinationDirectory`.
- `destinationDirectory`: The directory to contain the renamed object, which may be the same as `sourceDirectory`.
- `overItem`: The file system object if the destination exists, as discovered in a prior lookup. If this parameter is non-`nil`, mark `overItem` as deleted, so the file system can free its allocated space on the next call to [`reclaimItem(_:replyHandler:)`](fsvolume/handler/reclaimitem(_:replyhandler:).md). After doing so, ensure the operation finishes without errors.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If renaming succeeds, pass an instance of [`FSRenameItemResult`](fsrenameitemresult.md) containing the [`FSFileName`](fsfilename.md) as it exists within `destinationDirectory`, the [`FSItem.Attributes`](fsitem/attributes.md) of the renamed item, the updated [`FSItem.Attributes`](fsitem/attributes.md) of the source directory, the updated [`FSItem.Attributes`](fsitem/attributes.md) of the destination directory, the [`FSItem.Attributes`](fsitem/attributes.md) of the overwritten item (if any), and the volume’s updated free space, along with a `nil` error. If renaming fails, pass the relevant error as the second parameter; FSKit ignores the [`FSRenameItemResult`](fsrenameitemresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

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
- [class FSRenameItemResult](fsrenameitemresult.md)
  The result of a rename-item call.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/reclaimitem(_:replyhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/renameitem(_:indirectory:named:to:indirectory:overitem:context:replyhandler:))*