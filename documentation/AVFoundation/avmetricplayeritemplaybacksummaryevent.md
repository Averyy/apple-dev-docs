# AVMetricPlayerItemPlaybackSummaryEvent

**Framework**: AVFoundation  
**Kind**: class

An event that represents the combined metrics for the entire playback session.

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
class AVMetricPlayerItemPlaybackSummaryEvent
```

## Topics

### Inspecting the event
- [var errorEvent: AVMetricErrorEvent?](avmetricplayeritemplaybacksummaryevent/errorevent.md)
- [var mediaResourceRequestCount: Int](avmetricplayeritemplaybacksummaryevent/mediaresourcerequestcount.md)
- [var playbackDuration: Int](avmetricplayeritemplaybacksummaryevent/playbackduration.md)
- [var recoverableErrorCount: Int](avmetricplayeritemplaybacksummaryevent/recoverableerrorcount.md)
- [var stallCount: Int](avmetricplayeritemplaybacksummaryevent/stallcount.md)
- [var timeSpentInInitialStartup: TimeInterval](avmetricplayeritemplaybacksummaryevent/timespentininitialstartup.md)
- [var timeSpentRecoveringFromStall: TimeInterval](avmetricplayeritemplaybacksummaryevent/timespentrecoveringfromstall.md)
- [var timeWeightedAverageBitrate: Int](avmetricplayeritemplaybacksummaryevent/timeweightedaveragebitrate.md)
- [var timeWeightedPeakBitrate: Int](avmetricplayeritemplaybacksummaryevent/timeweightedpeakbitrate.md)
- [var variantSwitchCount: Int](avmetricplayeritemplaybacksummaryevent/variantswitchcount.md)

## Relationships

### Inherits From
- [AVMetricEvent](avmetricevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md)
  An event that represents when the playback rate changes.
- [class AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md)
  An event that represents when the playback seek completes.
- [class AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md)
  An event that represents when a playback seek occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemplaybacksummaryevent)*