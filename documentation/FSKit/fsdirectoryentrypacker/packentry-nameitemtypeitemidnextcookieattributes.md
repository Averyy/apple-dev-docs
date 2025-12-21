# packEntry(name:itemType:itemID:nextCookie:attributes:)

**Framework**: FSKit  
**Kind**: method

Provides a directory entry during enumeration.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func packEntry(name: FSFileName, itemType: FSItem.ItemType, itemID: FSItem.Identifier, nextCookie: FSDirectoryCookie, attributes: FSItem.Attributes?) -> Bool
```

#### Return Value

`true` (Swift) or `YES` (Objective-C) if packing was successful and enumeration can continue with the next directory entry. If the value is `false` (Swift) or `NO` (Objective-C), stop enumerating. This result can happen when the entry is too big for the remaining space in the buffer.

#### Discussion

You call this method in your implementation of [`enumerateDirectory(_:startingAt:verifier:attributes:packer:replyHandler:)`](fsvolume/operations/enumeratedirectory(_:startingat:verifier:attributes:packer:replyhandler:).md), for each directory entry you want to provide to the enumeration.

## Parameters

- `name`: The item’s name.
- `itemType`: The type of the item.
- `itemID`: The item’s identifier. Typically this is an inode number, or one of the constants defined by   like  .
- `nextCookie`: A value to indicate the next entry in the directory to enumerate. FSKit passes this value as the   parameter on the next call to  . Use whatever value is appropriate for your implementation; the value is opaque to FSKit.
- `attributes`: The item’s attributes. Pass   if the enumeration call didn’t request attributes.

## See Also

- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.Identifier](fsitem/identifier.md)
  The unique identifier for an item.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdirectoryentrypacker/packentry(name:itemtype:itemid:nextcookie:attributes:))*