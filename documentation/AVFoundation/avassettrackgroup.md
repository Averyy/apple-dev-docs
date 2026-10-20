# AVAssetTrackGroup

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAssetTrackGroup : NSObject
```

#### Overview

A track group describes a group of related alternative tracks, only one of which should play at a time. Groups of alternative tracks typically contain variations of the same content, like subtitles in multiple translations.

You can inspect an asset’s track groups by loading the value of its [`trackGroups`](./avpartialasyncproperty/trackgroups.md) property.

## Topics

### Getting track ID values
- [var trackIDs: [NSNumber]](./avassettrackgroup/trackids.md)
  The IDs of the tracks in the group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
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

### Assets
- [class AVAsset](./avasset.md)
  An object that models timed audiovisual media.
- [class AVURLAsset](./avurlasset.md)
  An asset that represents media at a local or remote URL.
- [class AVAssetTrack](./avassettrack.md)
  An object that models a track of media that an asset contains.
- [class AVAssetTrackSegment](./avassettracksegment.md)
  An object that represents a time range segment of an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackgroup)*