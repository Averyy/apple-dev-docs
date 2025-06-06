# timeResolution

**Framework**: AVFAudio  
**Kind**: property

The time resolution value for the sequence, in ticks (pulses) per quarter note.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var timeResolution: Int { get }
```

#### Discussion

If you use a MIDI file to construct the containing sequence, the resolution is the contents of the file. If you want to keep a time resolution when writing a new file, retrieve this value and then specify it when writing to an audio sequencer. It doesn’t affect the rendering or notion of time of the sequence — only it’s MIDI file representation.

By default, the framework sets this value to `480` when creating the sequence manually, or to a value from a MIDI file if you use it to create the sequence.

You can only retrieve this value from the tempo track.

## See Also

- [var isMuted: Bool](avmusictrack/ismuted.md)
  A Boolean value that indicates whether the track is in a muted state.
- [var isSoloed: Bool](avmusictrack/issoloed.md)
  A Boolean value that indicates whether the track is in a soloed state.
- [var offsetTime: AVMusicTimeStamp](avmusictrack/offsettime.md)
  The offset of the track’s start time, in beats.
- [var usesAutomatedParameters: Bool](avmusictrack/usesautomatedparameters.md)
  A Boolean value that indicates whether the track is an automation track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/timeresolution)*