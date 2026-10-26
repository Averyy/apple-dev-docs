# init(asset:mindingInterval:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a fragmented asset minder that monitors the specified asset at the indicated minding interval.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(asset: any AVAsset & AVFragmentMinding, mindingInterval: TimeInterval)
```

```objc
- (instancetype) initWithAsset:(AVAsset<AVFragmentMinding> *) asset mindingInterval:(NSTimeInterval) mindingInterval;
```

#### Return Value

The new fragmented asset minder.

## Parameters

- `asset`: The fragmented asset added to the fragmented asset minder.
- `mindingInterval`: The amount of time between checking to see if the system appended additional fragments to the minded asset.

## See Also

### Creating an asset minder
- [+ fragmentedAssetMinderWithAsset:mindingInterval:](./fragmentedassetminderwithasset_mindinginterval_.md)
  Creates a fragmented asset minder containing the specified asset and minding interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/init(asset:mindinginterval:))*