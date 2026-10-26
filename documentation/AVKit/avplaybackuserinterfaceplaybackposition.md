# AVPlaybackUserInterfacePlaybackPosition

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A snapshot comprising a playback position recorded at a known host time and the rate of position advancement.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class AVPlaybackUserInterfacePlaybackPosition
```

```objc
@interface AVPlaybackUserInterfacePlaybackPosition : NSObject
```

#### Overview

All three fields must be captured atomically by the conformer.

## Topics

### Initializers
- [init?(coder: NSCoder)](./avplaybackuserinterfaceplaybackposition/init%28coder%29.md)
- [init(position: CMTime, hostTime: CMTime, rate: Float)](./avplaybackuserinterfaceplaybackposition/init%28position,hosttime,rate%29.md)
  Creates a new playback position snapshot.
### Instance Properties
- [var hostTime: CMTime](./avplaybackuserinterfaceplaybackposition/hosttime.md)
  The mach host time at which `position` was accurate.
- [var position: CMTime](./avplaybackuserinterfaceplaybackposition/position.md)
  The playback position at the time of the snapshot.
- [var rate: Float](./avplaybackuserinterfaceplaybackposition/rate.md)
  The rate of position advancement at the time of the snapshot. Zero when paused; negative during reverse scan.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Timeline and segments
- [protocol AVPlaybackUserInterfaceTimeControllable](./avplaybackuserinterfacetimecontrollable-50vcy.md)
  Provides time control and navigation capabilities for media content.
- [class AVPlaybackUserInterfaceTimelineSegment](./avplaybackuserinterfacetimelinesegment.md)
  Represents a contiguous segment of timeline content with specific playback characteristics.
- [enum AVPlaybackUserInterfaceTimelineSegmentType](./avplaybackuserinterfacetimelinesegmenttype.md)
  Describes the type of content within a timeline segment.
- [AVPlaybackUserInterfaceTimeControllable](./avplaybackuserinterfacetimecontrollable-62fq2.md)
  Provides time control and navigation capabilities for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackposition)*