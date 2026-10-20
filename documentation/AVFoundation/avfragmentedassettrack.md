# AVFragmentedAssetTrack

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVFragmentedAssetTrack : AVAssetTrack
```

#### Overview

This class subclasses [`AVAssetTrack`](./avassettrack.md). It has no methods or properties of its own.

## Relationships

### Inherits From
- [AVAssetTrack](./avassettrack.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](./avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Fragmented assets
- [class AVFragmentedAsset](./avfragmentedasset.md)
  An asset with a duration that the system can extend without modifying its existing media data.
- [class AVFragmentedAssetMinder](./avfragmentedassetminder.md)
  An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [protocol AVFragmentMinding](./avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedassettrack)*