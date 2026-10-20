# AVMetricPlayerItemSeekDidCompleteEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An event that represents when the playback seek completes.

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
class AVMetricPlayerItemSeekDidCompleteEvent
```

```objc
@interface AVMetricPlayerItemSeekDidCompleteEvent : AVMetricPlayerItemRateChangeEvent
```

## Topics

### Inspecting the event
- [var didSeekInBuffer: Bool](./avmetricplayeritemseekdidcompleteevent/didseekinbuffer.md)

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

### Transport control
- [class AVMetricPlayerItemPlaybackSummaryEvent](./avmetricplayeritemplaybacksummaryevent.md)
  An event that represents the combined metrics for the entire playback session.
- [class AVMetricPlayerItemRateChangeEvent](./avmetricplayeritemratechangeevent.md)
  An event that represents when the playback rate changes.
- [class AVMetricPlayerItemSeekEvent](./avmetricplayeritemseekevent.md)
  An event that represents when a playback seek occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemseekdidcompleteevent)*