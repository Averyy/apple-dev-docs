# renameItem(_:inDirectory:named:to:inDirectory:overItem:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Renames an item from one path in the file system to another.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func renameItem(_ item: FSItem, inDirectory sourceDirectory: FSItem, named sourceName: FSFileName, to destinationName: FSFileName, inDirectory destinationDirectory: FSItem, overItem: FSItem?) async throws -> FSFileName
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
- `destinationName`: The new name of the item as it appears in  .
- `destinationDirectory`: The directory to contain the renamed object, which may be the same as  .
- `overItem`: The file system object if the destination exists, as discovered in a prior lookup. If this parameter is non- , mark   as deleted, so the file system can free its allocated space on the next call to  . After doing so, ensure the operation finishes without errors.
- `reply`: A block or closure to indicate success or failure. If renaming succeeds, pass the   as it exists within   and a   error. If renaming fails, pass the relevant error as the second parameter; FSKit ignores any   in this case. For an   Swift implementation, there’s no reply handler; simply return the   or throw an error.

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
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/renameitem(_:indirectory:named:to:indirectory:overitem:replyhandler:))*