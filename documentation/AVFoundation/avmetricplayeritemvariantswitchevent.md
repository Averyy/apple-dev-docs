# AVMetricPlayerItemVariantSwitchEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An event that represents when the player completes a variant switch.

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
class AVMetricPlayerItemVariantSwitchEvent
```

```objc
@interface AVMetricPlayerItemVariantSwitchEvent : AVMetricEvent
```

## Topics

### Inspecting the event
- [var didSucceed: Bool](./avmetricplayeritemvariantswitchevent/didsucceed.md)
- [var fromVariant: AVAssetVariant?](./avmetricplayeritemvariantswitchevent/fromvariant.md)
- [var loadedTimeRanges: [CMTimeRange]](./avmetricplayeritemvariantswitchevent/loadedtimeranges-5lkmg.md)
- [var toVariant: AVAssetVariant](./avmetricplayeritemvariantswitchevent/tovariant.md)
- [var audioRendition: AVMetricMediaRendition](./avmetricplayeritemvariantswitchevent/audiorendition.md)
  Represents the currently selected video rendition’s identifiers.
- [var videoRendition: AVMetricMediaRendition](./avmetricplayeritemvariantswitchevent/videorendition.md)
  Represents the currently selected video rendition’s identifiers.
- [var subtitleRendition: AVMetricMediaRendition](./avmetricplayeritemvariantswitchevent/subtitlerendition.md)
  Represents the currently selected audio rendition’s identifiers.
- [loadedTimeRanges](./avmetricplayeritemvariantswitchevent/loadedtimeranges-4rhjw.md)

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
- [class AVMetricContentKeyRequestEvent](./avmetriccontentkeyrequestevent.md)
  An event that represents a live streaming content key resource request.
- [class AVMetricHLSMediaSegmentRequestEvent](./avmetrichlsmediasegmentrequestevent.md)
  An event that represents a live streaming media segment resource request.
- [class AVMetricHLSPlaylistRequestEvent](./avmetrichlsplaylistrequestevent.md)
  An event that represents a live streaming playlist resource request.
- [class AVMetricPlayerItemVariantSwitchStartEvent](./avmetricplayeritemvariantswitchstartevent.md)
  An event that represents when the player attempts a variant switch.
- [class AVMetricMediaRendition](./avmetricmediarendition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemvariantswitchevent)*