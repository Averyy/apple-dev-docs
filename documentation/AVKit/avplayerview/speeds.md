# speeds

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A list of user-selectable playback speeds to show in the playback speed control.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var speeds: [AVPlaybackSpeed] { get set }
```

```objc
@property (copy) NSArray<AVPlaybackSpeed *> * speeds;
```

## Discussion

By default, this property value equals [`systemDefaultSpeeds`](../avplaybackspeed/systemdefaultspeeds.md). Setting this property to an empty array hides the playback speed selection user interface.

To set the playback speed programmatically, call the [`selectSpeed(_:)`](./selectspeed%28_%29.md) method, or set the value of the [`defaultRate`](../../AVFoundation/avplayer/defaultrate.md) property on the view controller’s associated [`AVPlayer`](../../AVFoundation/avplayer.md) object.

## See Also

### Configuring the playback speed
- [var selectedSpeed: AVPlaybackSpeed?](./selectedspeed.md)
  The currently selected playback speed.
- [func selectSpeed(AVPlaybackSpeed)](./selectspeed%28_%29.md)
  Selects a specified playback speed.
- [class AVPlaybackSpeed](../avplaybackspeed.md)
  An object that represents a user-selectable playback speed in a playback user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/speeds)*