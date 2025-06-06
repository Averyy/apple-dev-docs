# duration

**Framework**: Avfoundation  
**Kind**: property

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

#### Discussion

This property indicates the duration of the item, not considering either its [`forwardPlaybackEndTime`](avplayeritem/forwardplaybackendtime.md) or [`reversePlaybackEndTime`](avplayeritem/reverseplaybackendtime.md).

The system reports the value of this property as [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite) until it loads the duration of the underlying asset. There are two ways to make sure you don’t access the value of duration until the system makes it available:

- Wait until the [`status`](avplayeritem/status-swift.property.md) of the player item is [`AVPlayerItem.Status.readyToPlay`](avplayeritem/status-swift.enum/readytoplay.md).
- Register for key-value observation of the property and request the initial value. If the system reports the initial value as [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite), wait for the player item to notify you when [`duration`](avplayeritem/duration.md) becomes available.

> **Note**:  The value of [`duration`](avplayeritem/duration.md) may remain [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite) for live streams.

## See Also

- [func currentTime() -> CMTime](avplayeritem/currenttime.md)
  Returns the current time of the item.
- [func currentDate() -> Date?](avplayeritem/currentdate.md)
  Returns the current time of the item as a date.
- [var timebase: CMTimebase?](avplayeritem/timebase.md)
  The timebase information for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/duration)*