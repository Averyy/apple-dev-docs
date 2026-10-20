# AVFragmentedAssetMinder

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that periodically checks whether the system adds new fragments to a fragmented asset.

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
class AVFragmentedAssetMinder
```

```objc
@interface AVFragmentedAssetMinder : NSObject
```

## Topics

### Creating an asset minder
- [init(asset: any AVAsset & AVFragmentMinding, mindingInterval: TimeInterval)](./avfragmentedassetminder/init%28asset,mindinginterval%29.md)
  Creates a fragmented asset minder that monitors the specified asset at the indicated minding interval.
### Configuring the minding interval
- [var mindingInterval: TimeInterval](./avfragmentedassetminder/mindinginterval.md)
  An interval that specifies when to perform a check for additional fragments.
### Inspecting a fragment asset
- [var assets: [any AVAsset & AVFragmentMinding]](./avfragmentedassetminder/assets.md)
  The minded array of fragmented assets.
### Adding and removing fragmented assets
- [func addFragmentedAsset(any AVAsset & AVFragmentMinding)](./avfragmentedassetminder/addfragmentedasset%28_%29.md)
  Adds a fragmented asset to the array of minded assets.
- [func removeFragmentedAsset(any AVAsset & AVFragmentMinding)](./avfragmentedassetminder/removefragmentedasset%28_%29.md)
  Removes a fragmented asset from the array of minded assets.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVFragmentedMovieMinder](./avfragmentedmovieminder.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Fragmented assets
- [class AVFragmentedAsset](./avfragmentedasset.md)
  An asset with a duration that the system can extend without modifying its existing media data.
- [class AVFragmentedAssetTrack](./avfragmentedassettrack.md)
  An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [protocol AVFragmentMinding](./avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder)*