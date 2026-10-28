# assetCollectionSubtype

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The subtype of the asset collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var assetCollectionSubtype: PHAssetCollectionSubtype { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetCollectionSubtype assetCollectionSubtype;
```

## Discussion

Use subtypes to make minor distinctions between collections of the same type. For albums, for example, you might distinguish user-created albums from those synced from a Mac. See [`PHAssetCollectionSubtype`](../phassetcollectionsubtype.md) for possible values.

## See Also

### Reading Asset Collection Metadata
- [var assetCollectionType: PHAssetCollectionType](./assetcollectiontype.md)
  The type of the asset collection, such as an album or a moment.
- [enum PHAssetCollectionType](../phassetcollectiontype.md)
  Major distinctions between kinds of asset collections, used by the [`assetCollectionType`](./assetcollectiontype.md) property and the [`fetchAssetCollectionsContaining(_:with:options:)`](./fetchassetcollectionscontaining%28_,with,options%29.md) and [`fetchAssetCollections(with:subtype:options:)`](./fetchassetcollections%28with,subtype,options%29.md) methods.
- [enum PHAssetCollectionSubtype](../phassetcollectionsubtype.md)
  Minor distinctions between kinds of asset collections, used by the [`assetCollectionSubtype`](./assetcollectionsubtype.md) property and the [`fetchAssetCollections(with:subtype:options:)`](./fetchassetcollections%28with,subtype,options%29.md) method.
- [var estimatedAssetCount: Int](./estimatedassetcount.md)
  The estimated number of assets in the asset collection.
- [var startDate: Date?](./startdate.md)
  The earliest creation date among all assets in the asset collection.
- [var endDate: Date?](./enddate.md)
  The latest creation date among all assets in the asset collection.
- [var approximateLocation: CLLocation?](./approximatelocation.md)
  A location representing those of all assets in the collection.
- [var localizedLocationNames: [String]](./localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection/assetcollectionsubtype)*