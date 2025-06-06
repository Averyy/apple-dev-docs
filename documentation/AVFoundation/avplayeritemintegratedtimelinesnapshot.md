# AVPlayerItemIntegratedTimelineSnapshot

**Framework**: AVFoundation  
**Kind**: class

An immutable representation of inspectable details of an integrated timeline object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class AVPlayerItemIntegratedTimelineSnapshot
```

#### Overview

A snapshot doesn’t reflect the new timeline state as playback progresses. You can request a new snapshot instance from an [`AVPlayerItemIntegratedTimeline`](avplayeritemintegratedtimeline.md) that reflect the latest timeline state.

## Topics

### Inspecting the snapshot
- [var duration: CMTime](avplayeritemintegratedtimelinesnapshot/duration.md)
  The total duration of the primary item and scheduled interstitial events.
- [var currentSegment: AVPlayerItemSegment?](avplayeritemintegratedtimelinesnapshot/currentsegment.md)
  The currently playing segment.
- [var segments: [AVPlayerItemSegment]](avplayeritemintegratedtimelinesnapshot/segments.md)
  The segments for this snapshot.
- [class AVPlayerItemSegment](avplayeritemsegment.md)
  An immutable object that represents a segment of time on the integrated timeline.
- [var currentTime: CMTime](avplayeritemintegratedtimelinesnapshot/currenttime.md)
  The current time on the integrated timeline when the system created the snapshot.
- [var currentDate: Date?](avplayeritemintegratedtimelinesnapshot/currentdate.md)
  The current date on the integrated timeline when the system created the snapshot.
### Time mapping
- [func segmentAndOffsetIntoSegment(forTimelineTime: CMTime) -> (AVPlayerItemSegment, CMTime)](avplayeritemintegratedtimelinesnapshot/segmentandoffsetintosegment(fortimelinetime:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var currentSnapshot: AVPlayerItemIntegratedTimelineSnapshot](avplayeritemintegratedtimeline/currentsnapshot.md)
  An immutable representation of the timeline state at time of request.
- [class let snapshotsOutOfSyncNotification: NSNotification.Name](avplayeritemintegratedtimeline/snapshotsoutofsyncnotification.md)
  A notification the system posts when the snapshot objects provided by this timeline become out of sync with the current timeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot)*