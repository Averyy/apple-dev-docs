# selectedSpeed

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The currently selected playback speed.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var selectedSpeed: AVPlaybackSpeed? { get }
```

```objc
@property (readonly, nullable) AVPlaybackSpeed * selectedSpeed;
```

## Discussion

This value reflects the associated player’s [`defaultRate`](../../AVFoundation/avplayer/defaultrate.md) property value. If you set the [`defaultRate`](../../AVFoundation/avplayer/defaultrate.md) to a value that doesn’t match a speed contained in the [`speeds`](./speeds.md) property, the system sets this value to `nil`.

## See Also

### Configuring the playback speed
- [var speeds: [AVPlaybackSpeed]](./speeds.md)
  A list of user-selectable playback speeds to show in the playback speed control.
- [func selectSpeed(AVPlaybackSpeed)](./selectspeed%28_%29.md)
  Selects a specified playback speed.
- [class AVPlaybackSpeed](../avplaybackspeed.md)
  An object that represents a user-selectable playback speed in a playback user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/selectedspeed)*