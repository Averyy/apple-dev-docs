# currentTime

**Framework**: AppKit  
**Kind**: property

The sound’s playback progress, in seconds.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var currentTime: TimeInterval { get set }
```

#### Discussion

Sounds start with `currentTime == 0` and end with `currentTime == ([<sound> duration] - 1)`.

This property is not archived, copied, or stored on the pasteboard.

## See Also

- [var duration: TimeInterval](nssound/duration.md)
  The duration of the sound, in seconds.
- [var name: NSSound.Name?](nssound/name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](nssound/name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](nssound/setname(_:).md)
- [var volume: Float](nssound/volume.md)
  The volume of the sound.
- [var loops: Bool](nssound/loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](nssound/playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](nssound/playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/currenttime)*