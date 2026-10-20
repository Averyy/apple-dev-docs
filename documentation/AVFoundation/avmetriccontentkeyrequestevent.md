# AVMetricContentKeyRequestEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An event that represents a live streaming content key resource request.

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
class AVMetricContentKeyRequestEvent
```

```objc
@interface AVMetricContentKeyRequestEvent : AVMetricEvent
```

## Topics

### Inspecting the event
- [var contentKeySpecifier: AVContentKeySpecifier](./avmetriccontentkeyrequestevent/contentkeyspecifier.md)
- [var isClientInitiated: Bool](./avmetriccontentkeyrequestevent/isclientinitiated.md)
- [var mediaResourceRequestEvent: AVMetricMediaResourceRequestEvent?](./avmetriccontentkeyrequestevent/mediaresourcerequestevent.md)
- [var mediaType: AVMediaType](./avmetriccontentkeyrequestevent/mediatype.md)

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

### HTTP Live Streaming
- [class AVMetricMediaResourceRequestEvent](./avmetricmediaresourcerequestevent.md)
  An event that represents a media resource request.
- [class AVMetricHLSMediaSegmentRequestEvent](./avmetrichlsmediasegmentrequestevent.md)
  An event that represents a live streaming media segment resource request.
- [class AVMetricHLSPlaylistRequestEvent](./avmetrichlsplaylistrequestevent.md)
  An event that represents a live streaming playlist resource request.
- [class AVMetricPlayerItemVariantSwitchStartEvent](./avmetricplayeritemvariantswitchstartevent.md)
  An event that represents when the player attempts a variant switch.
- [class AVMetricPlayerItemVariantSwitchEvent](./avmetricplayeritemvariantswitchevent.md)
  An event that represents when the player completes a variant switch.
- [class AVMetricMediaRendition](./avmetricmediarendition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetriccontentkeyrequestevent)*