# PHCollectionListType

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Major distinctions between kinds of collection list, used by the [`collectionListType`](./phcollectionlist/collectionlisttype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./phcollectionlist/fetchcollectionlists%28with,subtype,options%29.md) method.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHCollectionListType
```

```c
enum PHCollectionListType : NSInteger;
```

## Topics

### Constants
- [PHCollectionListType.momentList](./phcollectionlisttype/momentlist.md)
  A group of asset collections of type [`PHAssetCollectionType.moment`](./phassetcollectiontype/moment.md).
- [PHCollectionListType.folder](./phcollectionlisttype/folder.md)
  A folder containing asset collections of type [`PHAssetCollectionType.album`](./phassetcollectiontype/album.md) or [`PHAssetCollectionType.smartAlbum`](./phassetcollectiontype/smartalbum.md).
- [PHCollectionListType.smartFolder](./phcollectionlisttype/smartfolder.md)
  A smart folder synced to the device from .
### Initializers
- [init?(rawValue: Int)](./phcollectionlisttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reading Collection List Metadata
- [var collectionListType: PHCollectionListType](./phcollectionlist/collectionlisttype.md)
  The type of asset collection group that the collection list represents.
- [var collectionListSubtype: PHCollectionListSubtype](./phcollectionlist/collectionlistsubtype.md)
  The type of asset collection grouping the collection list represents.
- [enum PHCollectionListSubtype](./phcollectionlistsubtype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListSubtype`](./phcollectionlist/collectionlistsubtype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./phcollectionlist/fetchcollectionlists%28with,subtype,options%29.md), [`fetchMomentLists(with:containingMoment:options:)`](./phcollectionlist/fetchmomentlists%28with,containingmoment,options%29.md), and [`fetchMomentLists(with:options:)`](./phcollectionlist/fetchmomentlists%28with,options%29.md) methods.
- [var startDate: Date?](./phcollectionlist/startdate.md)
  The earliest creation date among all assets in the collection list.
- [var endDate: Date?](./phcollectionlist/enddate.md)
  The latest creation date among all assets in the collection list.
- [var localizedLocationNames: [String]](./phcollectionlist/localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlisttype)*