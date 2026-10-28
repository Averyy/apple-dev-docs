# fragmentedAssetMinderWithAsset:mindingInterval:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a fragmented asset minder containing the specified asset and minding interval.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) fragmentedAssetMinderWithAsset:(AVAsset<AVFragmentMinding> *) asset mindingInterval:(NSTimeInterval) mindingInterval;
```

## Return Value

The new fragmented asset minder.

## Parameters

- `asset`: The fragmented asset added to the fragmented asset minder.
- `mindingInterval`: The amount of time between checking to see if the system appended additional fragments to the minded asset.

## See Also

### Creating an asset minder
- [init(asset: any AVAsset & AVFragmentMinding, mindingInterval: TimeInterval)](./init%28asset,mindinginterval%29.md)
  Creates a fragmented asset minder that monitors the specified asset at the indicated minding interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/fragmentedassetminderwithasset:mindinginterval:)*