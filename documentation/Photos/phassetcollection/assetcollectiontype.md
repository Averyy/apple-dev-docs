# assetCollectionType

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The type of the asset collection, such as an album or a moment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var assetCollectionType: PHAssetCollectionType { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetCollectionType assetCollectionType;
```

## Discussion

See [`PHAssetCollectionType`](../phassetcollectiontype.md) for possible values.

## See Also

### Reading Asset Collection Metadata
- [enum PHAssetCollectionType](../phassetcollectiontype.md)
  Major distinctions between kinds of asset collections, used by the [`assetCollectionType`](./assetcollectiontype.md) property and the [`fetchAssetCollectionsContaining(_:with:options:)`](./fetchassetcollectionscontaining%28_,with,options%29.md) and [`fetchAssetCollections(with:subtype:options:)`](./fetchassetcollections%28with,subtype,options%29.md) methods.
- [var assetCollectionSubtype: PHAssetCollectionSubtype](./assetcollectionsubtype.md)
  The subtype of the asset collection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection/assetcollectiontype)*