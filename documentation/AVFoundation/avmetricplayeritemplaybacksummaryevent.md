# AVMetricPlayerItemPlaybackSummaryEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMetricPlayerItemPlaybackSummaryEvent : AVMetricEvent
```

## Topics

### Inspecting the event
- [var errorEvent: AVMetricErrorEvent?](./avmetricplayeritemplaybacksummaryevent/errorevent.md)
- [var mediaResourceRequestCount: Int](./avmetricplayeritemplaybacksummaryevent/mediaresourcerequestcount.md)
- [var playbackDuration: Int](./avmetricplayeritemplaybacksummaryevent/playbackduration.md)
- [var recoverableErrorCount: Int](./avmetricplayeritemplaybacksummaryevent/recoverableerrorcount.md)
- [var stallCount: Int](./avmetricplayeritemplaybacksummaryevent/stallcount.md)
- [var timeSpentInInitialStartup: TimeInterval](./avmetricplayeritemplaybacksummaryevent/timespentininitialstartup.md)
- [var timeSpentRecoveringFromStall: TimeInterval](./avmetricplayeritemplaybacksummaryevent/timespentrecoveringfromstall.md)
- [var timeWeightedAverageBitrate: Int](./avmetricplayeritemplaybacksummaryevent/timeweightedaveragebitrate.md)
- [var timeWeightedPeakBitrate: Int](./avmetricplayeritemplaybacksummaryevent/timeweightedpeakbitrate.md)
- [var variantSwitchCount: Int](./avmetricplayeritemplaybacksummaryevent/variantswitchcount.md)

## Relationships

### Inherits From
- [AVMetricEvent](./avmetricevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Transport control
- [class AVMetricPlayerItemRateChangeEvent](./avmetricplayeritemratechangeevent.md)
  An event that represents when the playback rate changes.
- [class AVMetricPlayerItemSeekDidCompleteEvent](./avmetricplayeritemseekdidcompleteevent.md)
  An event that represents when the playback seek completes.
- [class AVMetricPlayerItemSeekEvent](./avmetricplayeritemseekevent.md)
  An event that represents when a playback seek occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemplaybacksummaryevent)*