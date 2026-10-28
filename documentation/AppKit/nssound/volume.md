# volume

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The volume of the sound.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var volume: Float { get set }
```

```objc
@property float volume;
```

## Discussion

The valid range is between `0.0` and `1.0`.

The value of this property does not affect the systemwide volume.

## See Also

### Configuring Sounds
- [var name: NSSound.Name?](./name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](./name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](./setname%28_%29.md)
- [var currentTime: TimeInterval](./currenttime.md)
  The sound’s playback progress, in seconds.
- [var loops: Bool](./loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](./playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](./playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/volume)*