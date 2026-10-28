# selectSpeed(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Selects a specified playback speed.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func selectSpeed(_ speed: AVPlaybackSpeed)
```

```objc
- (void) selectSpeed:(AVPlaybackSpeed *) speed;
```

## Discussion

If you call this method with a speed that isn’t contained in the [`speeds`](./speeds.md) property, the system ignores the call.

## Parameters

- `speed`: The playback speed to select.

## See Also

### Configuring the playback speed
- [var speeds: [AVPlaybackSpeed]](./speeds.md)
  A list of user-selectable playback speeds to show in the playback speed control.
- [var selectedSpeed: AVPlaybackSpeed?](./selectedspeed.md)
  The currently selected playback speed.
- [class AVPlaybackSpeed](../avplaybackspeed.md)
  An object that represents a user-selectable playback speed in a playback user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/selectspeed(_:))*