# userInfo

**Framework**: File Provider  
**Kind**: property

A property list that contains additional data about the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var userInfo: [AnyHashable : Any]? { get }
```

#### Discussion

The `userInfo` data is often used by the predicate for actions defined by the File Provider UI extension. For more information, see `Adding Actions to the Context Menu`.

The `userInfo` dictionary can only accept entries with numbers (including Boolean values), dates, or strings as either the key or the value.

## See Also

- [var extendedAttributes: [String : Data]](nsfileprovideritemprotocol/extendedattributes.md)
  The extended file attributes synced by the File Provider extension.
- [var fileSystemFlags: NSFileProviderFileSystemFlags](nsfileprovideritemprotocol/filesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [struct NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [var tagData: Data?](nsfileprovideritemprotocol/tagdata.md)
  An abstract data blob representing the tags associated with the item.
- [var favoriteRank: NSNumber?](nsfileprovideritemprotocol/favoriterank.md)
  A 64-bit, unsigned integer indicating the order of the favorite item in the Favorites list.
- [let NSFileProviderFavoriteRankUnranked: UInt64](nsfileproviderfavoriterankunranked.md)
  A value that indicates that the item is not ranked.
- [var typeAndCreator: NSFileProviderTypeAndCreator](nsfileprovideritemprotocol/typeandcreator.md)
  The file type and creator codes for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/userinfo)*