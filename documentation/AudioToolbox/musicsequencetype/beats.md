# MusicSequenceType.beats

**Framework**: Audio Toolbox  
**Kind**: case

Used for a music sequence that corresponds to a normal MIDI file. The tempo track defines the number of beats per second and can have multiple tempo events.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case beats
```

## See Also

- [MusicSequenceType.seconds](musicsequencetype/seconds.md)
  Used for a music sequence that corresponds to a MIDI file, but employs SMPTE timecode. The tempo track contains a single tempo event that specifies 60 beat-per-minute.
- [MusicSequenceType.samples](musicsequencetype/samples.md)
  Used for audio samples; a music sequence of this type cannot be saved to a MIDI file. The tempo track contains a single tempo event that specifies an audio sample rate in samples-per-second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/beats)*