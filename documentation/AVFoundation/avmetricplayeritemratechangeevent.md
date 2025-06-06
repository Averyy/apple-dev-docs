# AVMetricPlayerItemRateChangeEvent

**Framework**: AVFoundation  
**Kind**: class

An event that represents when the playback rate changes.

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
class AVMetricPlayerItemRateChangeEvent
```

## Topics

### Inspecting the event
- [var previousRate: Double](avmetricplayeritemratechangeevent/previousrate.md)
- [var rate: Double](avmetricplayeritemratechangeevent/rate.md)
- [var variant: AVAssetVariant?](avmetricplayeritemratechangeevent/variant.md)

## Relationships

### Inherits From
- [AVMetricEvent](avmetricevent.md)
### Inherited By
- [AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md)
- [AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md)
- [AVMetricPlayerItemStallEvent](avmetricplayeritemstallevent.md)
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

## See Also

- [class AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md)
  An event that represents the combined metrics for the entire playback session.
- [class AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md)
  An event that represents when the playback seek completes.
- [class AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md)
  An event that represents when a playback seek occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemratechangeevent)*