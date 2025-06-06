# selectSpeed(_:)

**Framework**: AVKit  
**Kind**: method

Selects a specified playback speed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func selectSpeed(_ speed: AVPlaybackSpeed)
```

#### Discussion

If you call this method with a speed that isn’t contained in the [`speeds`](avplayerviewcontroller/speeds.md) property, the system ignores the call.

## Parameters

- `speed`: The playback speed to select.

## See Also

- [var speeds: [AVPlaybackSpeed]](avplayerviewcontroller/speeds.md)
  A list of user-selectable playback speeds to show in the playback speed control.
- [var selectedSpeed: AVPlaybackSpeed?](avplayerviewcontroller/selectedspeed.md)
  The currently selected playback speed.
- [class AVPlaybackSpeed](avplaybackspeed.md)
  An object that represents a user-selectable playback speed in a playback user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/selectspeed(_:))*