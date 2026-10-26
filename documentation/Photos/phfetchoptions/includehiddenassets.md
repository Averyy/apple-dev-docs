# includeHiddenAssets

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the fetch result includes assets marked as hidden.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var includeHiddenAssets: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL includeHiddenAssets;
```

#### Discussion

If the value is `false` (the default), fetches exclude assets whose [`isHidden`](../phasset/ishidden.md) property is `true`. If the value is `true`, fetches include all assets regardless of their hidden state.

## See Also

### Limiting Fetch Results
- [var fetchLimit: Int](./fetchlimit.md)
  The maximum number of objects to include in the fetch result.
- [var includeAllBurstAssets: Bool](./includeallburstassets.md)
  A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [var includeAssetSourceTypes: PHAssetSourceType](./includeassetsourcetypes.md)
  The set of source types for which to include assets in the fetch result.
- [var prefetchAssetExtendedMetadata: Bool](./prefetchassetextendedmetadata.md)
  A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchoptions/includehiddenassets)*