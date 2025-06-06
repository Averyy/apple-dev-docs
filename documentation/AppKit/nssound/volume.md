# volume

**Framework**: AppKit  
**Kind**: property

The volume of the sound.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var volume: Float { get set }
```

#### Discussion

The valid range is between `0.0` and `1.0`.

The value of this property does not affect the systemwide volume.

## See Also

- [var name: NSSound.Name?](nssound/name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](nssound/name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](nssound/setname(_:).md)
- [var currentTime: TimeInterval](nssound/currenttime.md)
  The sound’s playback progress, in seconds.
- [var loops: Bool](nssound/loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](nssound/playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](nssound/playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/volume)*