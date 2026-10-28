# FSCreateItemResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a create-item call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSCreateItemResult
```

```objc
@interface FSCreateItemResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`createItem(named:type:in:attributes:context:replyHandler:)`](./fsvolume/handler/createitem%28named,type,in,attributes,context,replyhandler%29.md).

## Topics

### Creating a create-item result
- [init?(newItem: FSItem, newItemName: FSFileName, newItemAttributes: FSItem.Attributes, directoryAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](./fscreateitemresult/init%28newitem,newitemname,newitemattributes,directoryattributes,freespace%29.md)
  Creates a result for an item-creation operation.
- [class FSFileName](./fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](./fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Inherited By
- [FSCreateFileKOIOResult](./fscreatefilekoioresult.md)
- [FSCreateSymlinkResult](./fscreatesymlinkresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with items
- [func createItem(named: FSFileName, type: FSItem.ItemType, in: FSItem, attributes: FSItem.SetAttributesRequest, context: FSContext, replyHandler: (FSCreateItemResult?, (any Error)?) -> Void)](./fsvolume/handler/createitem%28named,type,in,attributes,context,replyhandler%29.md)
  Creates a new file or directory item.
- [class FSFileName](./fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](./fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](./fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSLookupItemResult?, (any Error)?) -> Void)](./fsvolume/handler/lookupitem%28named,in,context,replyhandler%29.md)
  Looks up an item within a directory.
- [class FSLookupItemResult](./fslookupitemresult.md)
  The result of an item lookup call.
- [func removeItem(FSItem, named: FSFileName, from: FSItem, context: FSContext, replyHandler: (FSRemoveItemResult?, (any Error)?) -> Void)](./fsvolume/handler/removeitem%28_,named,from,context,replyhandler%29.md)
  Removes an existing item from a given directory.
- [class FSRemoveItemResult](./fsremoveitemresult.md)
  The result of a remove-item call.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, context: FSContext, replyHandler: (FSRenameItemResult?, (any Error)?) -> Void)](./fsvolume/handler/renameitem%28_,indirectory,named,to,indirectory,overitem,context,replyhandler%29.md)
  Renames an item from one path in the file system to another.
- [class FSRenameItemResult](./fsrenameitemresult.md)
  The result of a rename-item call.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](./fsvolume/handler/reclaimitem%28_,replyhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreateitemresult)*