# loops

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var loops: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the sounds restarts playback when it finishes and does not send [`sound(_:didFinishPlaying:)`](nssounddelegate/sound(_:didfinishplaying:).md) to its delegate when it reaches the end of its content and restarts playback. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var name: NSSound.Name?](nssound/name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](nssound/name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](nssound/setname(_:).md)
- [var volume: Float](nssound/volume.md)
  The volume of the sound.
- [var currentTime: TimeInterval](nssound/currenttime.md)
  The sound’s playback progress, in seconds.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](nssound/playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](nssound/playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/loops)*