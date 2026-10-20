# playbackDeviceIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Identifies the sound’s output device

**Availability**:
- macOS 10.5+

## Declaration

```swift
var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier? { get set }
```

```objc
@property (copy, nullable) NSSoundPlaybackDeviceIdentifier playbackDeviceIdentifier;
```

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
- [var loops: Bool](./loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [typealias PlaybackDeviceIdentifier](./playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/playbackdeviceidentifier-swift.property)*