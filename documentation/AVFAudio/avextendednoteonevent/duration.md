# duration

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The duration of the event, in beats.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var duration: AVMusicTimeStamp { get set }
```

```objc
@property (readwrite) AVMusicTimeStamp duration;
```

## See Also

### Configuring a note-on event
- [var midiNote: Float](./midinote.md)
  The MIDI note number.
- [var velocity: Float](./velocity.md)
  The MDI velocity.
- [var instrumentID: UInt32](./instrumentid.md)
  The instrument identifier.
- [var groupID: UInt32](./groupid.md)
  The audio unit channel that handles the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/duration)*