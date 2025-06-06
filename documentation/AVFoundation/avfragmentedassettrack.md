# AVFragmentedAssetTrack

**Framework**: AVFoundation  
**Kind**: class

An object that provides the track-level interface to inspect a fragmented asset’s media tracks.

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
class AVFragmentedAssetTrack
```

#### Overview

This class subclasses [`AVAssetTrack`](avassettrack.md). It has no methods or properties of its own.

## Relationships

### Inherits From
- [AVAssetTrack](avassettrack.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVFragmentedAsset](avfragmentedasset.md)
  An asset with a duration that the system can extend without modifying its existing media data.
- [class AVFragmentedAssetMinder](avfragmentedassetminder.md)
  An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [protocol AVFragmentMinding](avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedassettrack)*