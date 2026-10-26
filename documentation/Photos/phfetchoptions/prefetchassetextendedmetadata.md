# prefetchAssetExtendedMetadata

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var prefetchAssetExtendedMetadata: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL prefetchAssetExtendedMetadata;
```

#### Discussion

By default `extendedMetadata` is fetched on demand, with the dot accessor. Prefetching will fetch it as part of the `PHAsset` in a single fetch, rather than incurring fetch overhead for each `PHAsset`.

## See Also

### Limiting Fetch Results
- [var fetchLimit: Int](./fetchlimit.md)
  The maximum number of objects to include in the fetch result.
- [var includeAllBurstAssets: Bool](./includeallburstassets.md)
  A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [var includeHiddenAssets: Bool](./includehiddenassets.md)
  A Boolean value that determines whether the fetch result includes assets marked as hidden.
- [var includeAssetSourceTypes: PHAssetSourceType](./includeassetsourcetypes.md)
  The set of source types for which to include assets in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchoptions/prefetchassetextendedmetadata)*