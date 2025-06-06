# AVPlayerItemSegment

**Framework**: AVFoundation  
**Kind**: class

An immutable object that represents a segment of time on the integrated timeline.

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
class AVPlayerItemSegment
```

## Topics

### Identifying the type
- [var segmentType: AVPlayerItemSegment.SegmentType](avplayeritemsegment/segmenttype-swift.property.md)
  The type content this segment represents.
- [AVPlayerItemSegment.SegmentType](avplayeritemsegment/segmenttype-swift.enum.md)
  Constants that specify the type of segment.
### Inspecting the segment
- [var timeMapping: CMTimeMapping](avplayeritemsegment/timemapping.md)
  The time mapping for this segment.
- [var loadedTimeRanges: [CMTimeRange]](avplayeritemsegment/loadedtimeranges-879hc.md)
  The time ranges for the segment that have media data is readily available.
- [var startDate: Date?](avplayeritemsegment/startdate.md)
  The date at which a segment starts.
- [var interstitialEvent: AVPlayerInterstitialEvent?](avplayeritemsegment/interstitialevent.md)
  The associated interstitial event for this segment.

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

- [var duration: CMTime](avplayeritemintegratedtimelinesnapshot/duration.md)
  The total duration of the primary item and scheduled interstitial events.
- [var currentSegment: AVPlayerItemSegment?](avplayeritemintegratedtimelinesnapshot/currentsegment.md)
  The currently playing segment.
- [var segments: [AVPlayerItemSegment]](avplayeritemintegratedtimelinesnapshot/segments.md)
  The segments for this snapshot.
- [var currentTime: CMTime](avplayeritemintegratedtimelinesnapshot/currenttime.md)
  The current time on the integrated timeline when the system created the snapshot.
- [var currentDate: Date?](avplayeritemintegratedtimelinesnapshot/currentdate.md)
  The current date on the integrated timeline when the system created the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsegment)*