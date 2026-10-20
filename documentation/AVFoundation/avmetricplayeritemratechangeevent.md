# AVMetricPlayerItemRateChangeEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An event that represents when the playback rate changes.

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
class AVMetricPlayerItemRateChangeEvent
```

```objc
@interface AVMetricPlayerItemRateChangeEvent : AVMetricEvent
```

## Topics

### Inspecting the event
- [var previousRate: Double](./avmetricplayeritemratechangeevent/previousrate.md)
- [var rate: Double](./avmetricplayeritemratechangeevent/rate.md)
- [var variant: AVAssetVariant?](./avmetricplayeritemratechangeevent/variant.md)

## Relationships

### Inherits From
- [AVMetricEvent](./avmetricevent.md)
### Inherited By
- [AVMetricPlayerItemSeekDidCompleteEvent](./avmetricplayeritemseekdidcompleteevent.md)
- [AVMetricPlayerItemSeekEvent](./avmetricplayeritemseekevent.md)
- [AVMetricPlayerItemStallEvent](./avmetricplayeritemstallevent.md)
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

### Transport control
- [class AVMetricPlayerItemPlaybackSummaryEvent](./avmetricplayeritemplaybacksummaryevent.md)
  An event that represents the combined metrics for the entire playback session.
- [class AVMetricPlayerItemSeekDidCompleteEvent](./avmetricplayeritemseekdidcompleteevent.md)
  An event that represents when the playback seek completes.
- [class AVMetricPlayerItemSeekEvent](./avmetricplayeritemseekevent.md)
  An event that represents when a playback seek occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemratechangeevent)*