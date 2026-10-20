# removeFragmentedAsset(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a fragmented asset from the array of minded assets.

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
func removeFragmentedAsset(_ asset: any AVAsset & AVFragmentMinding)
```

```objc
- (void) removeFragmentedAsset:(AVAsset<AVFragmentMinding> *) asset;
```

## Parameters

- `asset`: The fragmented asset to remove from the minder.

## See Also

### Adding and removing fragmented assets
- [func addFragmentedAsset(any AVAsset & AVFragmentMinding)](./addfragmentedasset%28_%29.md)
  Adds a fragmented asset to the array of minded assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/removefragmentedasset(_:))*