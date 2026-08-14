# AVPlaybackUserInterfacePlaybackPosition

**Framework**: AVKit  
**Kind**: class

A snapshot comprising a playback position recorded at a known host time and the rate of position advancement.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class AVPlaybackUserInterfacePlaybackPosition
```

#### Overview

All three fields must be captured atomically by the conformer.

## Topics

### Initializers
- [init?(coder: NSCoder)](avplaybackuserinterfaceplaybackposition/init(coder:).md)
- [init(position: CMTime, hostTime: CMTime, rate: Float)](avplaybackuserinterfaceplaybackposition/init(position:hosttime:rate:).md)
  Creates a new playback position snapshot.
### Instance Properties
- [var hostTime: CMTime](avplaybackuserinterfaceplaybackposition/hosttime.md)
  The mach host time at which `position` was accurate.
- [var position: CMTime](avplaybackuserinterfaceplaybackposition/position.md)
  The playback position at the time of the snapshot.
- [var rate: Float](avplaybackuserinterfaceplaybackposition/rate.md)
  The rate of position advancement at the time of the snapshot. Zero when paused; negative during reverse scan.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md)
  Provides time control and navigation capabilities for media content.
- [class AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimelinesegment.md)
  Represents a contiguous segment of timeline content with specific playback characteristics.
- [enum AVPlaybackUserInterfaceTimelineSegmentType](avplaybackuserinterfacetimelinesegmenttype.md)
  Describes the type of content within a timeline segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackposition)*