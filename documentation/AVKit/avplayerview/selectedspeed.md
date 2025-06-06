# selectedSpeed

**Framework**: AVKit  
**Kind**: property

The currently selected playback speed.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var selectedSpeed: AVPlaybackSpeed? { get }
```

#### Discussion

This value reflects the associated player’s [`defaultRate`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/defaultRate) property value. If you set the [`defaultRate`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/defaultRate) to a value that doesn’t match a speed contained in the [`speeds`](avplayerview/speeds.md) property, the system sets this value to `nil`.

## See Also

- [var speeds: [AVPlaybackSpeed]](avplayerview/speeds.md)
  A list of user-selectable playback speeds to show in the playback speed control.
- [func selectSpeed(AVPlaybackSpeed)](avplayerview/selectspeed(_:).md)
  Selects a specified playback speed.
- [class AVPlaybackSpeed](avplaybackspeed.md)
  An object that represents a user-selectable playback speed in a playback user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/selectedspeed)*