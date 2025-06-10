# AVMetricMediaResourceRequestEvent

**Framework**: AVFoundation  
**Kind**: class

An event that represents a media resource request.

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
class AVMetricMediaResourceRequestEvent
```

## Topics

### Inspecting the event
- [var byteRange: NSRange](avmetricmediaresourcerequestevent/byterange.md)
- [var errorEvent: AVMetricErrorEvent?](avmetricmediaresourcerequestevent/errorevent.md)
- [var networkTransactionMetrics: URLSessionTaskMetrics?](avmetricmediaresourcerequestevent/networktransactionmetrics.md)
- [var requestEndTime: Date](avmetricmediaresourcerequestevent/requestendtime.md)
- [var requestStartTime: Date](avmetricmediaresourcerequestevent/requeststarttime.md)
- [var responseEndTime: Date](avmetricmediaresourcerequestevent/responseendtime.md)
- [var responseStartTime: Date](avmetricmediaresourcerequestevent/responsestarttime.md)
- [var serverAddress: String?](avmetricmediaresourcerequestevent/serveraddress.md)
- [var url: URL?](avmetricmediaresourcerequestevent/url.md)
- [var wasReadFromCache: Bool](avmetricmediaresourcerequestevent/wasreadfromcache.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricmediaresourcerequestevent)*