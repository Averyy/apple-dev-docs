# estimatedAssetCount

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The estimated number of assets in the asset collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var estimatedAssetCount: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSUInteger estimatedAssetCount;
```

## Discussion

This count may not match the current number of assets in the collection. To get the most recent count, fetch the collection’s assets with the [`fetchAssets(in:options:)`](../phasset/fetchassets%28in,options%29.md) method and read the [`count`](../phfetchresult/count.md) property of the fetch result.

If asset count information is not available for the collection, this property’s value is `NSNotFound`.

## See Also

### Reading Asset Collection Metadata
- [var assetCollectionType: PHAssetCollectionType](./assetcollectiontype.md)
  The type of the asset collection, such as an album or a moment.
- [enum PHAssetCollectionType](../phassetcollectiontype.md)
  Major distinctions between kinds of asset collections, used by the [`assetCollectionType`](./assetcollectiontype.md) property and the [`fetchAssetCollectionsContaining(_:with:options:)`](./fetchassetcollectionscontaining%28_,with,options%29.md) and [`fetchAssetCollections(with:subtype:options:)`](./fetchassetcollections%28with,subtype,options%29.md) methods.
- [var assetCollectionSubtype: PHAssetCollectionSubtype](./assetcollectionsubtype.md)
  The subtype of the asset collection.
- [enum PHAssetCollectionSubtype](../phassetcollectionsubtype.md)
  Minor distinctions between kinds of asset collections, used by the [`assetCollectionSubtype`](./assetcollectionsubtype.md) property and the [`fetchAssetCollections(with:subtype:options:)`](./fetchassetcollections%28with,subtype,options%29.md) method.
- [var startDate: Date?](./startdate.md)
  The earliest creation date among all assets in the asset collection.
- [var endDate: Date?](./enddate.md)
  The latest creation date among all assets in the asset collection.
- [var approximateLocation: CLLocation?](./approximatelocation.md)
  A location representing those of all assets in the collection.
- [var localizedLocationNames: [String]](./localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection/estimatedassetcount)*