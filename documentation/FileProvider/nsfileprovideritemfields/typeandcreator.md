# typeAndCreator

**Framework**: File Provider  
**Kind**: property

The file type and creator codes for the item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static var typeAndCreator: NSFileProviderItemFields { get }
```

#### Discussion

This property contains two values: the file type code and the creator code. The system synchronizes both codes at the same time, so define both, even if you’re just changing one.

If you modify this property, the system sets the [`NSFileProviderTypeAndCreator`](nsfileprovidertypeandcreator.md) value passed to the [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md) or [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md) methods. The system also writes the type and creator codes in the `FileInfo` structure, if relevant.

## See Also

- [static var extendedAttributes: NSFileProviderItemFields](nsfileprovideritemfields/extendedattributes.md)
  The item’s extended attributes.
- [static var fileSystemFlags: NSFileProviderItemFields](nsfileprovideritemfields/filesystemflags.md)
  The flags describing the item’s on-disk representation.
- [static var tagData: NSFileProviderItemFields](nsfileprovideritemfields/tagdata.md)
  The tags for the item.
- [static var favoriteRank: NSFileProviderItemFields](nsfileprovideritemfields/favoriterank.md)
  The item’s favorite rank.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemfields/typeandcreator)*