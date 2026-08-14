# AVMetricHLSPlaylistRequestEvent

**Framework**: AVFoundation  
**Kind**: class

An event that represents a live streaming playlist resource request.

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
class AVMetricHLSPlaylistRequestEvent
```

## Topics

### Inspecting the event
- [var isMultivariantPlaylist: Bool](avmetrichlsplaylistrequestevent/ismultivariantplaylist.md)
- [var mediaResourceRequestEvent: AVMetricMediaResourceRequestEvent?](avmetrichlsplaylistrequestevent/mediaresourcerequestevent.md)
- [var mediaType: AVMediaType](avmetrichlsplaylistrequestevent/mediatype.md)
- [var url: URL?](avmetrichlsplaylistrequestevent/url.md)

## Relationships

### Inherits From
- [AVMetricEvent](avmetricevent.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVMetricMediaResourceRequestEvent](avmetricmediaresourcerequestevent.md)
  An event that represents a media resource request.
- [class AVMetricContentKeyRequestEvent](avmetriccontentkeyrequestevent.md)
  An event that represents a live streaming content key resource request.
- [class AVMetricHLSMediaSegmentRequestEvent](avmetrichlsmediasegmentrequestevent.md)
  An event that represents a live streaming media segment resource request.
- [class AVMetricPlayerItemVariantSwitchStartEvent](avmetricplayeritemvariantswitchstartevent.md)
  An event that represents when the player attempts a variant switch.
- [class AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md)
  An event that represents when the player completes a variant switch.
- [class AVMetricMediaRendition](avmetricmediarendition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetrichlsplaylistrequestevent)*