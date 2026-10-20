# name

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name assigned to the sound.

**Availability**:
- macOS

## Declaration

```swift
var name: NSSound.Name? { get }
```

```objc
@property (copy, readonly, nullable) NSSoundName name;
```

#### Discussion

The value of this property is `nil` when no name has been assigned.

## See Also

### Configuring Sounds
- [typealias Name](./name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](./setname%28_%29.md)
- [var volume: Float](./volume.md)
  The volume of the sound.
- [var currentTime: TimeInterval](./currenttime.md)
  The sound’s playback progress, in seconds.
- [var loops: Bool](./loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](./playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](./playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/name-swift.property)*