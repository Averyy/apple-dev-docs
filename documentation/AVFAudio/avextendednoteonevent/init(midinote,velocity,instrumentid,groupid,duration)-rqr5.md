# init(midiNote:velocity:instrumentID:groupID:duration:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a note on event with the default instrument.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(midiNote: Float, velocity: Float, instrumentID: UInt32, groupID: UInt32, duration: AVMusicTimeStamp)
```

```objc
- (instancetype) initWithMIDINote:(float) midiNote velocity:(float) velocity instrumentID:(UInt32) instrumentID groupID:(UInt32) groupID duration:(AVMusicTimeStamp) duration;
```

## Discussion

Use [`defaultInstrument`](./defaultinstrument.md) when you set `instrumentID`.

## Parameters

- `midiNote`: The MIDI note number.
- `velocity`: The MIDI velocity.
- `instrumentID`: The default instrument.
- `groupID`: The identifier that represents the audio unit channel that handles the event.
- `duration`: The duration of the event, in beats.

## See Also

### Creating a note-on event
- [init(midiNote: Float, velocity: Float, groupID: UInt32, duration: AVMusicTimeStamp)](./init%28midinote,velocity,groupid,duration%29-60hve.md)
  Creates an event with a MIDI note, velocity, group identifier, and duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/init(midinote:velocity:instrumentid:groupid:duration:)-rqr5)*