# PHAssetCollectionType

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Major distinctions between kinds of asset collections, used by the [`assetCollectionType`](./phassetcollection/assetcollectiontype.md) property and the [`fetchAssetCollectionsContaining(_:with:options:)`](./phassetcollection/fetchassetcollectionscontaining%28_,with,options%29.md) and [`fetchAssetCollections(with:subtype:options:)`](./phassetcollection/fetchassetcollections%28with,subtype,options%29.md) methods.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHAssetCollectionType
```

```c
enum PHAssetCollectionType : NSInteger;
```

## Topics

### Constants
- [PHAssetCollectionType.album](./phassetcollectiontype/album.md)
  An album in the Photos app.
- [PHAssetCollectionType.smartAlbum](./phassetcollectiontype/smartalbum.md)
  A smart album whose contents update dynamically.
- [PHAssetCollectionType.moment](./phassetcollectiontype/moment.md)
  A moment in the Photos app.
### Initializers
- [init?(rawValue: Int)](./phassetcollectiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reading Asset Collection Metadata
- [var assetCollectionType: PHAssetCollectionType](./phassetcollection/assetcollectiontype.md)
  The type of the asset collection, such as an album or a moment.
- [var assetCollectionSubtype: PHAssetCollectionSubtype](./phassetcollection/assetcollectionsubtype.md)
  The subtype of the asset collection.
- [enum PHAssetCollectionSubtype](./phassetcollectionsubtype.md)
  Minor distinctions between kinds of asset collections, used by the [`assetCollectionSubtype`](./phassetcollection/assetcollectionsubtype.md) property and the [`fetchAssetCollections(with:subtype:options:)`](./phassetcollection/fetchassetcollections%28with,subtype,options%29.md) method.
- [var estimatedAssetCount: Int](./phassetcollection/estimatedassetcount.md)
  The estimated number of assets in the asset collection.
- [var startDate: Date?](./phassetcollection/startdate.md)
  The earliest creation date among all assets in the asset collection.
- [var endDate: Date?](./phassetcollection/enddate.md)
  The latest creation date among all assets in the asset collection.
- [var approximateLocation: CLLocation?](./phassetcollection/approximatelocation.md)
  A location representing those of all assets in the collection.
- [var localizedLocationNames: [String]](./phassetcollection/localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectiontype)*