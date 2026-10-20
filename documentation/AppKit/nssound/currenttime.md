# currentTime

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The sound’s playback progress, in seconds.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var currentTime: TimeInterval { get set }
```

```objc
@property NSTimeInterval currentTime;
```

#### Discussion

Sounds start with `currentTime == 0` and end with `currentTime == ([<sound> duration] - 1)`.

This property is not archived, copied, or stored on the pasteboard.

## See Also

### Related Documentation
- [var duration: TimeInterval](./duration.md)
  The duration of the sound, in seconds.
### Configuring Sounds
- [var name: NSSound.Name?](./name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](./name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](./setname%28_%29.md)
- [var volume: Float](./volume.md)
  The volume of the sound.
- [var loops: Bool](./loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](./playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](./playbackdeviceidentifier-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/currenttime)*