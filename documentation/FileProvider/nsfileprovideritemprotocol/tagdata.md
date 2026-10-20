# tagData

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

An abstract data blob representing the tags associated with the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var tagData: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * tagData;
```

## See Also

### Managing Metadata
- [var extendedAttributes: [String : Data]](./extendedattributes.md)
  The extended file attributes synced by the File Provider extension.
- [var fileSystemFlags: NSFileProviderFileSystemFlags](./filesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [struct NSFileProviderFileSystemFlags](../nsfileproviderfilesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A property list that contains additional data about the item.
- [var favoriteRank: NSNumber?](./favoriterank.md)
  A 64-bit, unsigned integer indicating the order of the favorite item in the Favorites list.
- [let NSFileProviderFavoriteRankUnranked: UInt64](../nsfileproviderfavoriterankunranked.md)
  A value that indicates that the item is not ranked.
- [var typeAndCreator: NSFileProviderTypeAndCreator](./typeandcreator.md)
  The file type and creator codes for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/tagdata)*