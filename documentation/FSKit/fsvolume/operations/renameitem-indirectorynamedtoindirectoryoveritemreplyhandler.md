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
- `destinationName`: The new name of the item as it appears in `destinationDirectory`.
- `destinationDirectory`: The directory to contain the renamed object, which may be the same as `sourceDirectory`.
- `overItem`: The file system object if the destination exists, as discovered in a prior lookup. If this parameter is non-`nil`, mark `overItem` as deleted, so the file system can free its allocated space on the next call to `reclaimItem(_:)`. After doing so, ensure the operation finishes without errors.
- `reply`: A block or closure to indicate success or failure. If renaming succeeds, pass the [`FSFileName`](fsfilename.md) as it exists within `destinationDirectory` and a `nil` error. If renaming fails, pass the relevant error as the second parameter; FSKit ignores any [`FSFileName`](fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSFileName`](fsfilename.md) or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/renameitem(_:indirectory:named:to:indirectory:overitem:replyhandler:))*