# AVMetricPlayerItemStallEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An event that represents when playback stalls.

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
class AVMetricPlayerItemStallEvent
```

```objc
@interface AVMetricPlayerItemStallEvent : AVMetricPlayerItemRateChangeEvent
```

## Relationships

### Inherits From
- [AVMetricPlayerItemRateChangeEvent](./avmetricplayeritemratechangeevent.md)
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

### Buffering
- [class AVMetricPlayerItemLikelyToKeepUpEvent](./avmetricplayeritemlikelytokeepupevent.md)
  An event that represents when playback is likely to continue without stalling.
- [class AVMetricPlayerItemInitialLikelyToKeepUpEvent](./avmetricplayeriteminitiallikelytokeepupevent.md)
  An event that represents the initial state for whether playback is likely to continue without stalling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemstallevent)*