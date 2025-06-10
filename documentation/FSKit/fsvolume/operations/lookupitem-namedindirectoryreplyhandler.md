# lookupItem(named:inDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Looks up an item within a directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func lookupItem(named name: FSFileName, inDirectory directory: FSItem) async throws -> (FSItem, FSFileName)
```

#### Discussion

If no item matching `name` exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and a code of `ENOENT`.

> 💡 **Tip**: The [`FSFileName`](fsfilename.md) sent back to the caller may differ from the `name` parameter. This flexibility allows your implementation to handle case-insensitive and case-sensitive file systems. It might also be the case that `name` uses a composed Unicode string, but the name maintained by the file system and provided to the caller is uncomposed Unicode.

## Parameters

- `name`: The name of the item to look up.
- `directory`: The directory in which to look up the item.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass the found   and its   (as saved within the file system), along with a   error. If lookup fails, pass the relevant error as the third parameter; any   or   are ignored in this case. For an   Swift implementation, there’s no reply handler; simply return the   and   as a tuple or throw an error.

## See Also

- [func createItem(named: FSFileName, type: FSItem.ItemType, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createitem(named:type:indirectory:attributes:replyhandler:).md)
  Creates a new file or directory item.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func removeItem(FSItem, named: FSFileName, fromDirectory: FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/removeitem(_:named:fromdirectory:replyhandler:).md)
  Removes an existing item from a given directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/renameitem(_:indirectory:named:to:indirectory:overitem:replyhandler:).md)
  Renames an item from one path in the file system to another.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/lookupitem(named:indirectory:replyhandler:))*