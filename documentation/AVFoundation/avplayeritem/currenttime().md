# currentTime()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the current time of the item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
func currentTime() -> CMTime
```

```objc
- (CMTime) currentTime;
```

## Mentions

- [Controlling the transport behavior of a player](../controlling-the-transport-behavior-of-a-player.md)

#### Return Value

The current time of the item.

## See Also

### Accessing timing information
- [func currentDate() -> Date?](./currentdate%28%29.md)
  Returns the current time of the item as a date.
- [var duration: CMTime](./duration.md)
  The duration of the item.
- [var timebase: CMTimebase?](./timebase.md)
  The timebase information for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/currenttime())*