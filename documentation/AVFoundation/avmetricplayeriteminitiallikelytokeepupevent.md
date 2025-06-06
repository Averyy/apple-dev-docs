# AVMetricPlayerItemInitialLikelyToKeepUpEvent

**Framework**: AVFoundation  
**Kind**: class

An event that represents the initial state for whether playback is likely to continue without stalling.

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
class AVMetricPlayerItemInitialLikelyToKeepUpEvent
```

## Topics

### Inspecting the event
- [var contentKeyRequestEvents: [AVMetricContentKeyRequestEvent]](avmetricplayeriteminitiallikelytokeepupevent/contentkeyrequestevents.md)
- [var mediaSegmentRequestEvents: [AVMetricHLSMediaSegmentRequestEvent]](avmetricplayeriteminitiallikelytokeepupevent/mediasegmentrequestevents.md)
- [var playlistRequestEvents: [AVMetricHLSPlaylistRequestEvent]](avmetricplayeriteminitiallikelytokeepupevent/playlistrequestevents.md)

## Relationships

### Inherits From
- [AVMetricPlayerItemLikelyToKeepUpEvent](avmetricplayeritemlikelytokeepupevent.md)
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

- [class AVMetricPlayerItemStallEvent](avmetricplayeritemstallevent.md)
  An event that represents when playback stalls.
- [class AVMetricPlayerItemLikelyToKeepUpEvent](avmetricplayeritemlikelytokeepupevent.md)
  An event that represents when playback is likely to continue without stalling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeriteminitiallikelytokeepupevent)*