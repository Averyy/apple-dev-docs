# createItem(named:type:inDirectory:attributes:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new file or directory item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func createItem(named name: FSFileName, type: FSItem.ItemType, inDirectory directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest) async throws -> (FSItem, FSFileName)
```

#### Discussion

If an item named `name` already exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and a code of `EEXIST`.

## Parameters

- `name`: The new item’s name.
- `type`: The new item’s type.  Valid values are   or  .
- `directory`: The directory in which to create the item.
- `newAttributes`: Attributes to apply to the new item.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass the newly-created   and its  , along with a   error. If creation fails, pass the relevant error as the third parameter; FSKit ignores any   or   in this case. For an   Swift implementation, there’s no reply handler; simply return a tuple of the   and its   or throw an error.

## See Also

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
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/createitem(named:type:indirectory:attributes:replyhandler:))*