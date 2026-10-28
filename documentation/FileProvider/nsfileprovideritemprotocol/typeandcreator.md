# typeAndCreator

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

The file type and creator codes for the item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
optional var typeAndCreator: NSFileProviderTypeAndCreator { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderTypeAndCreator typeAndCreator;
```

## Discussion

This property contains two values: the file type code and the creator code. The system synchronizes both codes at the same time, so define both, even if you’re just changing one.

If you modify this property, the system sets the [`NSFileProviderTypeAndCreator`](../nsfileprovidertypeandcreator.md) value passed to the [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](../nsfileproviderreplicatedextension/createitem%28basedon,fields,contents,options,request,completionhandler%29.md) or [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](../nsfileproviderreplicatedextension/modifyitem%28_,baseversion,changedfields,contents,options,request,completionhandler%29.md) methods. The system also writes the type and creator codes in the `FileInfo` structure, if relevant.

## See Also

### Managing Metadata
- [var extendedAttributes: [String : Data]](./extendedattributes.md)
  The extended file attributes synced by the File Provider extension.
- [var fileSystemFlags: NSFileProviderFileSystemFlags](./filesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [struct NSFileProviderFileSystemFlags](../nsfileproviderfilesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [var tagData: Data?](./tagdata.md)
  An abstract data blob representing the tags associated with the item.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A property list that contains additional data about the item.
- [var favoriteRank: NSNumber?](./favoriterank.md)
  A 64-bit, unsigned integer indicating the order of the favorite item in the Favorites list.
- [let NSFileProviderFavoriteRankUnranked: UInt64](../nsfileproviderfavoriterankunranked.md)
  A value that indicates that the item is not ranked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/typeandcreator)*