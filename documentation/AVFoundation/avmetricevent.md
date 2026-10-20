# AVMetricEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A base class that represents a metric event.

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
class AVMetricEvent
```

```objc
@interface AVMetricEvent : NSObject
```

## Topics

### Inspecting an event
- [var date: Date](./avmetricevent/date.md)
- [var mediaTime: CMTime](./avmetricevent/mediatime.md)
- [var sessionID: String?](./avmetricevent/sessionid.md)
### Initializers
- [init?(coder: NSCoder)](./avmetricevent/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVMetricContentKeyRequestEvent](./avmetriccontentkeyrequestevent.md)
- [AVMetricDownloadSummaryEvent](./avmetricdownloadsummaryevent.md)
- [AVMetricErrorEvent](./avmetricerrorevent.md)
- [AVMetricHLSMediaSegmentRequestEvent](./avmetrichlsmediasegmentrequestevent.md)
- [AVMetricHLSPlaylistRequestEvent](./avmetrichlsplaylistrequestevent.md)
- [AVMetricMediaResourceRequestEvent](./avmetricmediaresourcerequestevent.md)
- [AVMetricPlaybackModeSwitchEvent](./avmetricplaybackmodeswitchevent.md)
- [AVMetricPlayerItemLikelyToKeepUpEvent](./avmetricplayeritemlikelytokeepupevent.md)
- [AVMetricPlayerItemPlaybackSummaryEvent](./avmetricplayeritemplaybacksummaryevent.md)
- [AVMetricPlayerItemRateChangeEvent](./avmetricplayeritemratechangeevent.md)
- [AVMetricPlayerItemVariantSwitchEvent](./avmetricplayeritemvariantswitchevent.md)
- [AVMetricPlayerItemVariantSwitchStartEvent](./avmetricplayeritemvariantswitchstartevent.md)
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

### Metrics
- [struct AVMetrics](./avmetrics.md)
  An asynchronous stream of metric information.
- [struct AVMergedMetrics](./avmergedmetrics.md)
  An asynchronous stream of metric information from different publishers.
- [class AVVideoPerformanceMetrics](./avvideoperformancemetrics.md)
  An object that provides metrics related to video playback quality.
- [protocol AVMetricEventStreamPublisher](./avmetriceventstreampublisher.md)
  A type for objects that publish metric events to the event stream.
- [class AVMetricErrorEvent](./avmetricerrorevent.md)
  An object that represents a metric event when an error occurs.
- [Metric event types](./metric-event-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricevent)*