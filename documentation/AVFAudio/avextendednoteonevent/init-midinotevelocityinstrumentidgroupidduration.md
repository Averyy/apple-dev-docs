# init(midiNote:velocity:instrumentID:groupID:duration:)

**Framework**: AVFAudio  
**Kind**: init

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

#### Discussion

Use [`defaultInstrument`](avextendednoteonevent/defaultinstrument.md) when you set `instrumentID`.

## Parameters

- `midiNote`: The MIDI note number.
- `velocity`: The MIDI velocity.
- `instrumentID`: The default instrument.
- `groupID`: The identifier that represents the audio unit channel that handles the event.
- `duration`: The duration of the event, in beats.

## See Also

- [init(midiNote: Float, velocity: Float, groupID: UInt32, duration: AVMusicTimeStamp)](avextendednoteonevent/init(midinote:velocity:groupid:duration:).md)
  Creates an event with a MIDI note, velocity, group identifier, and duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/init(midinote:velocity:instrumentid:groupid:duration:))*