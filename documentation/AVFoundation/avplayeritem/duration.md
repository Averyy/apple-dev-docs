# duration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The duration of the item.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var duration: CMTime { get }
```

```objc
@property (readonly) CMTime duration;
```

#### Discussion

This property indicates the duration of the item, not considering either its [`forwardPlaybackEndTime`](./forwardplaybackendtime.md) or [`reversePlaybackEndTime`](./reverseplaybackendtime.md).

The system reports the value of this property as [`indefinite`](../../CoreMedia/cmtime/indefinite.md) until it loads the duration of the underlying asset. There are two ways to make sure you don’t access the value of duration until the system makes it available:

- Wait until the [`status`](./status-swift.property.md) of the player item is [`AVPlayerItem.Status.readyToPlay`](./status-swift.enum/readytoplay.md).
- Register for key-value observation of the property and request the initial value. If the system reports the initial value as [`indefinite`](../../CoreMedia/cmtime/indefinite.md), wait for the player item to notify you when [`duration`](./duration.md) becomes available.

> **Note**:  The value of [`duration`](./duration.md) may remain [`indefinite`](../../CoreMedia/cmtime/indefinite.md) for live streams.

## See Also

### Accessing timing information
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time of the item.
- [func currentDate() -> Date?](./currentdate%28%29.md)
  Returns the current time of the item as a date.
- [var timebase: CMTimebase?](./timebase.md)
  The timebase information for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/duration)*