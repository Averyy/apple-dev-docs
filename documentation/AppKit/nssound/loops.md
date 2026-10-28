# loops

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var loops: Bool { get set }
```

```objc
@property BOOL loops;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the sounds restarts playback when it finishes and does not send [`sound(_:didFinishPlaying:)`](../nssounddelegate/sound%28_,didfinishplaying%29.md) to its delegate when it reaches the end of its content and restarts playback. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring Sounds
- [var name: NSSound.Name?](./name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](./name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](./setname%28_%29.md)
- [var volume: Float](./volume.md)
  The volume of the sound.
- [var currentTime: TimeInterval](./currenttime.md)
  The sound’s playback progress, in seconds.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](./playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](./playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/loops)*