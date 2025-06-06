# Metric event types

**Framework**: AVFoundation

## Topics

### HTTP Live Streaming
- [class AVMetricMediaResourceRequestEvent](avmetricmediaresourcerequestevent.md)
  An event that represents a media resource request.
- [class AVMetricContentKeyRequestEvent](avmetriccontentkeyrequestevent.md)
  An event that represents a live streaming content key resource request.
- [class AVMetricHLSMediaSegmentRequestEvent](avmetrichlsmediasegmentrequestevent.md)
  An event that represents a live streaming media segment resource request.
- [class AVMetricHLSPlaylistRequestEvent](avmetrichlsplaylistrequestevent.md)
  An event that represents a live streaming playlist resource request.
- [class AVMetricPlayerItemVariantSwitchStartEvent](avmetricplayeritemvariantswitchstartevent.md)
  An event that represents when the player attempts a variant switch.
- [class AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md)
  An event that represents when the player completes a variant switch.
### Buffering
- [class AVMetricPlayerItemStallEvent](avmetricplayeritemstallevent.md)
  An event that represents when playback stalls.
- [class AVMetricPlayerItemLikelyToKeepUpEvent](avmetricplayeritemlikelytokeepupevent.md)
  An event that represents when playback is likely to continue without stalling.
- [class AVMetricPlayerItemInitialLikelyToKeepUpEvent](avmetricplayeriteminitiallikelytokeepupevent.md)
  An event that represents the initial state for whether playback is likely to continue without stalling.
### Transport control
- [class AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md)
  An event that represents the combined metrics for the entire playback session.
- [class AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md)
  An event that represents when the playback rate changes.
- [class AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md)
  An event that represents when the playback seek completes.
- [class AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md)
  An event that represents when a playback seek occurs.

## See Also

- [struct AVMetrics](avmetrics.md)
  An asynchronous stream of metric information.
- [struct AVMergedMetrics](avmergedmetrics.md)
  An asynchronous stream of metric information from different publishers.
- [class AVVideoPerformanceMetrics](avvideoperformancemetrics.md)
  An object that provides metrics related to video playback quality.
- [protocol AVMetricEventStreamPublisher](avmetriceventstreampublisher.md)
  A type for objects that publish metric events to the event stream.
- [class AVMetricEvent](avmetricevent.md)
  A base class that represents a metric event.
- [class AVMetricErrorEvent](avmetricerrorevent.md)
  An object that represents a metric event when an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/metric-event-types)*