# setName(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS

## Declaration

```swift
func setName(_ string: NSSound.Name?) -> Bool
```

```objc
- (BOOL) setName:(NSSoundName) string;
```

## See Also

### Configuring Sounds
- [var name: NSSound.Name?](./name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](./name-swift.typealias.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/setname(_:))*