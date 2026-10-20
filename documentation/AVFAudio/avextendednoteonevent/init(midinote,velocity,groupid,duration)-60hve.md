# init(midiNote:velocity:groupID:duration:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an event with a MIDI note, velocity, group identifier, and duration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(midiNote: Float, velocity: Float, groupID: UInt32, duration: AVMusicTimeStamp)
```

```objc
- (instancetype) initWithMIDINote:(float) midiNote velocity:(float) velocity groupID:(UInt32) groupID duration:(AVMusicTimeStamp) duration;
```

## Parameters

- `midiNote`: The MIDI note number.
- `velocity`: The MIDI velocity.
- `groupID`: The identifier that represents the audio unit channel that handles the event.
- `duration`: The duration of the event, in beats.

## See Also

### Creating a note-on event
- [init(midiNote: Float, velocity: Float, instrumentID: UInt32, groupID: UInt32, duration: AVMusicTimeStamp)](./init%28midinote,velocity,instrumentid,groupid,duration%29-rqr5.md)
  Creates a note on event with the default instrument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/init(midinote:velocity:groupid:duration:)-60hve)*