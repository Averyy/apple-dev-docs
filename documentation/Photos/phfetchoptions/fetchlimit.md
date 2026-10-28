# fetchLimit

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The maximum number of objects to include in the fetch result.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var fetchLimit: Int { get set }
```

```objc
@property (nonatomic, assign, readwrite) NSUInteger fetchLimit;
```

## Discussion

With the default fetch limit of zero, Photos returns all requested assets or collections in a fetch result. Change this value to fetch more efficiently in situations where a potentially very large result is not needed. For example, to fetch only the most recently captured asset, call the [`fetchAssets(with:)`](../phasset/fetchassets%28with%29.md) method, using the [`sortDescriptors`](./sortdescriptors.md) property to sort in descending date order, and setting a fetch limit of one.

## See Also

### Limiting Fetch Results
- [var includeAllBurstAssets: Bool](./includeallburstassets.md)
  A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [var includeHiddenAssets: Bool](./includehiddenassets.md)
  A Boolean value that determines whether the fetch result includes assets marked as hidden.
- [var includeAssetSourceTypes: PHAssetSourceType](./includeassetsourcetypes.md)
  The set of source types for which to include assets in the fetch result.
- [var prefetchAssetExtendedMetadata: Bool](./prefetchassetextendedmetadata.md)
  A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchoptions/fetchlimit)*