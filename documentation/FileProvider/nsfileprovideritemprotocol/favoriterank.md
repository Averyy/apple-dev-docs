# favoriteRank

**Framework**: File Provider  
**Kind**: property

A 64-bit, unsigned integer indicating the order of the favorite item in the Favorites list.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
optional var favoriteRank: NSNumber? { get }
```

## See Also

- [var extendedAttributes: [String : Data]](nsfileprovideritemprotocol/extendedattributes.md)
  The extended file attributes synced by the File Provider extension.
- [var fileSystemFlags: NSFileProviderFileSystemFlags](nsfileprovideritemprotocol/filesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [struct NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [var tagData: Data?](nsfileprovideritemprotocol/tagdata.md)
  An abstract data blob representing the tags associated with the item.
- [var userInfo: [AnyHashable : Any]?](nsfileprovideritemprotocol/userinfo.md)
  A property list that contains additional data about the item.
- [let NSFileProviderFavoriteRankUnranked: UInt64](nsfileproviderfavoriterankunranked.md)
  A value that indicates that the item is not ranked.
- [var typeAndCreator: NSFileProviderTypeAndCreator](nsfileprovideritemprotocol/typeandcreator.md)
  The file type and creator codes for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/favoriterank)*