# lookupItem(named:in:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Looks up an item within a directory.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func lookupItem(named name: FSFileName, in directory: FSItem, context: FSContext) async throws -> FSLookupItemResult
```

#### Discussion

If no item matching `name` exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/foundation/nsposixerrordomain) and a code of `ENOENT`.

> 💡 **Tip**: The [`FSFileName`](fsfilename.md) sent back to the caller may differ from the `name` parameter. This flexibility allows your implementation to handle case-insensitive and case-sensitive file systems. It might also be the case that `name` uses a composed Unicode string, but the name maintained by the file system and provided to the caller is uncomposed Unicode.

## Parameters

- `name`: The name of the item to look up.
- `directory`: The directory in which to look up the item.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass an instance of [`FSLookupItemResult`](fslookupitemresult.md) containing the found [`FSItem`](fsitem.md), its [`FSFileName`](fsfilename.md) (as saved within the file system), and its [`FSItem.Attributes`](fsitem/attributes.md), along with a `nil` error. If lookup fails, pass the relevant error as the second parameter; FSKit ignores the [`FSLookupItemResult`](fslookupitemresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/lookupitem(named:in:context:replyhandler:))*