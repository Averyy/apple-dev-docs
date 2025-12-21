# AVAssetTrackGroup

**Framework**: AVFoundation  
**Kind**: class

A group of related tracks in an asset.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVAssetTrackGroup
```

#### Overview

A track group describes a group of related alternative tracks, only one of which should play at a time. Groups of alternative tracks typically contain variations of the same content, like subtitles in multiple translations.

You can inspect an asset’s track groups by loading the value of its [`trackGroups`](avpartialasyncproperty/trackgroups.md) property.

## Topics

### Getting track ID values
- [var trackIDs: [NSNumber]](avassettrackgroup/trackids.md)
  The IDs of the tracks in the group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVAsset](avasset.md)
  An object that models timed audiovisual media.
- [class AVURLAsset](avurlasset.md)
  An asset that represents media at a local or remote URL.
- [class AVAssetTrack](avassettrack.md)
  An object that models a track of media that an asset contains.
- [class AVAssetTrackSegment](avassettracksegment.md)
  An object that represents a time range segment of an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackgroup)*