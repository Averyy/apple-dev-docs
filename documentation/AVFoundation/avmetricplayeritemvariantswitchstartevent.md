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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemvariantswitchstartevent)*