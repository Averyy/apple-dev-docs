# speeds

**Framework**: AVKit  
**Kind**: property

A list of user-selectable playback speeds to show in the playback speed control.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var speeds: [AVPlaybackSpeed] { get set }
```

#### Discussion

By default, this property value equals [`systemDefaultSpeeds`](avplaybackspeed/systemdefaultspeeds.md). Setting this property to an empty array hides the playback speed selection user interface.

To set the playback speed programmatically, call the [`selectSpeed(_:)`](avplayerview/selectspeed(_:).md) method, or set the value of the [`defaultRate`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/defaultRate) property on the view controller’s associated [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object.

## See Also

- [var selectedSpeed: AVPlaybackSpeed?](avplayerview/selectedspeed.md)
  The currently selected playback speed.
- [func selectSpeed(AVPlaybackSpeed)](avplayerview/selectspeed(_:).md)
  Selects a specified playback speed.
- [class AVPlaybackSpeed](avplaybackspeed.md)
  An object that represents a user-selectable playback speed in a playback user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/speeds)*