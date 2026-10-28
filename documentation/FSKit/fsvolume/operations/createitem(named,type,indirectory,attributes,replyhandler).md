# createItem(named:type:inDirectory:attributes:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new file or directory item.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func createItem(named name: FSFileName, type: FSItem.ItemType, inDirectory directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest, replyHandler reply: @escaping @Sendable (FSItem?, FSFileName?, (any Error)?) -> Void)
```

```swift
func createItem(named name: FSFileName, type: FSItem.ItemType, inDirectory directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest) async throws -> (FSItem, FSFileName)
```

```objc
- (void) createItemNamed:(FSFileName *) name type:(FSItemType) type inDirectory:(FSItem *) directory attributes:(FSItemSetAttributesRequest *) newAttributes replyHandler:(void (^)(FSItem *newItem, FSFileName *newItemName, NSError *error)) reply;
```

## Discussion

If an item named `name` already exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](../../../Foundation/nsposixerrordomain.md) and a code of `EEXIST`.

## Parameters

- `name`: The new item’s name.
- `type`: The new item’s type.  Valid values are [`FSItem.ItemType.file`](../../fsitem/itemtype/file.md) or [`FSItem.ItemType.directory`](../../fsitem/itemtype/directory.md).
- `directory`: The directory in which to create the item.
- `newAttributes`: Attributes to apply to the new item.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass the newly-created [`FSItem`](../../fsitem.md) and its [`FSFileName`](../../fsfilename.md), along with a `nil` error. If creation fails, pass the relevant error as the third parameter; FSKit ignores any [`FSItem`](../../fsitem.md) or [`FSFileName`](../../fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return a tuple of the [`FSItem`](../../fsitem.md) and its [`FSFileName`](../../fsfilename.md) or throw an error.

## See Also

### Working with items
- [class FSFileName](../../fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](../../fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](../../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(named: FSFileName, inDirectory: FSItem, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./lookupitem%28named,indirectory,replyhandler%29.md)
  Looks up an item within a directory.
- [func removeItem(FSItem, named: FSFileName, fromDirectory: FSItem, replyHandler: ((any Error)?) -> Void)](./removeitem%28_,named,fromdirectory,replyhandler%29.md)
  Removes an existing item from a given directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](./renameitem%28_,indirectory,named,to,indirectory,overitem,replyhandler%29.md)
  Renames an item from one path in the file system to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/createitem(named:type:indirectory:attributes:replyhandler:))*