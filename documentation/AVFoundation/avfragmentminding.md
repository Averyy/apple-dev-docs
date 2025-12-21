# AVFragmentMinding

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines whether an asset supports fragment minding.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol AVFragmentMinding
```

## Topics

### Fragment minder association
- [var isAssociatedWithFragmentMinder: Bool](avfragmentminding/isassociatedwithfragmentminder.md)
  A Boolean value that indicates whether an asset that supports fragment minding is currently associated with a fragment minder.

## Relationships

### Conforming Types
- [AVFragmentedAsset](avfragmentedasset.md)
- [AVFragmentedMovie](avfragmentedmovie.md)

## See Also

- [class AVFragmentedAsset](avfragmentedasset.md)
  An asset with a duration that the system can extend without modifying its existing media data.
- [class AVFragmentedAssetTrack](avfragmentedassettrack.md)
  An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [class AVFragmentedAssetMinder](avfragmentedassetminder.md)
  An object that periodically checks whether the system adds new fragments to a fragmented asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentminding)*