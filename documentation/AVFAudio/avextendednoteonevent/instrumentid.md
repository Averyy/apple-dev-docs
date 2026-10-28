# instrumentID

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The instrument identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instrumentID: UInt32 { get set }
```

```objc
@property (readwrite) UInt32 instrumentID;
```

## Discussion

Set this value to [`defaultInstrument`](./defaultinstrument.md).

## See Also

### Configuring a note-on event
- [var midiNote: Float](./midinote.md)
  The MIDI note number.
- [var velocity: Float](./velocity.md)
  The MDI velocity.
- [var groupID: UInt32](./groupid.md)
  The audio unit channel that handles the event.
- [var duration: AVMusicTimeStamp](./duration.md)
  The duration of the event, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/instrumentid)*