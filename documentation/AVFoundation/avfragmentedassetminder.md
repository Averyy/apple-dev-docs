# AVFragmentedAssetMinder

**Framework**: AVFoundation  
**Kind**: class

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

## Topics

### Creating an asset minder
- [init(asset: any AVAsset & AVFragmentMinding, mindingInterval: TimeInterval)](avfragmentedassetminder/init(asset:mindinginterval:).md)
  Creates a fragmented asset minder that monitors the specified asset at the indicated minding interval.
### Configuring the minding interval
- [var mindingInterval: TimeInterval](avfragmentedassetminder/mindinginterval.md)
  An interval that specifies when to perform a check for additional fragments.
### Inspecting a fragment asset
- [var assets: [any AVAsset & AVFragmentMinding]](avfragmentedassetminder/assets.md)
  The minded array of fragmented assets.
### Adding and removing fragmented assets
- [func addFragmentedAsset(any AVAsset & AVFragmentMinding)](avfragmentedassetminder/addfragmentedasset(_:).md)
  Adds a fragmented asset to the array of minded assets.
- [func removeFragmentedAsset(any AVAsset & AVFragmentMinding)](avfragmentedassetminder/removefragmentedasset(_:).md)
  Removes a fragmented asset from the array of minded assets.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVFragmentedMovieMinder](avfragmentedmovieminder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVFragmentedAsset](avfragmentedasset.md)
  An asset with a duration that the system can extend without modifying its existing media data.
- [class AVFragmentedAssetTrack](avfragmentedassettrack.md)
  An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [protocol AVFragmentMinding](avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder)*