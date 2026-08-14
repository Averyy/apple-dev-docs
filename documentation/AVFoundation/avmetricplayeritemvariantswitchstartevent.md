# AVMetricPlayerItemVariantSwitchStartEvent

**Framework**: AVFoundation  
**Kind**: class

An event that represents when the player attempts a variant switch.

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
class AVMetricPlayerItemVariantSwitchStartEvent
```

## Topics

### Inspecting the event
- [var fromVariant: AVAssetVariant?](avmetricplayeritemvariantswitchstartevent/fromvariant.md)
- [var loadedTimeRanges: [CMTimeRange]](avmetricplayeritemvariantswitchstartevent/loadedtimeranges-2mbm7.md)
- [var toVariant: AVAssetVariant](avmetricplayeritemvariantswitchstartevent/tovariant.md)
- [var audioRendition: AVMetricMediaRendition](avmetricplayeritemvariantswitchstartevent/audiorendition.md)
- [var videoRendition: AVMetricMediaRendition](avmetricplayeritemvariantswitchstartevent/videorendition.md)
- [var subtitleRendition: AVMetricMediaRendition](avmetricplayeritemvariantswitchstartevent/subtitlerendition.md)

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
- [class AVMetricHLSPlaylistRequestEvent](avmetrichlsplaylistrequestevent.md)
  An event that represents a live streaming playlist resource request.
- [class AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md)
  An event that represents when the player completes a variant switch.
- [class AVMetricMediaRendition](avmetricmediarendition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemvariantswitchstartevent)*