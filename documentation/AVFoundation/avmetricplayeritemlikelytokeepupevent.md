# AVMetricPlayerItemLikelyToKeepUpEvent

**Framework**: AVFoundation  
**Kind**: class

An event that represents when playback is likely to continue without stalling.

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
class AVMetricPlayerItemLikelyToKeepUpEvent
```

## Topics

### Inspecting the event
- [var loadedTimeRanges: [CMTimeRange]](avmetricplayeritemlikelytokeepupevent/loadedtimeranges-8yzws.md)
- [var timeTaken: TimeInterval](avmetricplayeritemlikelytokeepupevent/timetaken.md)
- [var variant: AVAssetVariant?](avmetricplayeritemlikelytokeepupevent/variant.md)

## Relationships

### Inherits From
- [AVMetricEvent](avmetricevent.md)
### Inherited By
- [AVMetricPlayerItemInitialLikelyToKeepUpEvent](avmetricplayeriteminitiallikelytokeepupevent.md)
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

- [class AVMetricPlayerItemStallEvent](avmetricplayeritemstallevent.md)
  An event that represents when playback stalls.
- [class AVMetricPlayerItemInitialLikelyToKeepUpEvent](avmetricplayeriteminitiallikelytokeepupevent.md)
  An event that represents the initial state for whether playback is likely to continue without stalling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemlikelytokeepupevent)*