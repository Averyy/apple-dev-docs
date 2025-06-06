# name

**Framework**: AppKit  
**Kind**: property

The name assigned to the sound.

**Availability**:
- macOS ?+

## Declaration

```swift
var name: NSSound.Name? { get }
```

#### Discussion

The value of this property is `nil` when no name has been assigned.

## See Also

- [typealias Name](nssound/name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](nssound/setname(_:).md)
- [var volume: Float](nssound/volume.md)
  The volume of the sound.
- [var currentTime: TimeInterval](nssound/currenttime.md)
  The sound’s playback progress, in seconds.
- [var loops: Bool](nssound/loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](nssound/playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](nssound/playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/name-swift.property)*