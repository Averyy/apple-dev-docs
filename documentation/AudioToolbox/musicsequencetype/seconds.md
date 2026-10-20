# MusicSequenceType.seconds

**Framework**: Audio Toolbox  
**Kind**: case  
**Role**: Case

Used for a music sequence that corresponds to a MIDI file, but employs SMPTE timecode. The tempo track contains a single tempo event that specifies 60 beat-per-minute.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case seconds
```

```c
kMusicSequenceType_Seconds
```

## See Also

### Constants
- [MusicSequenceType.beats](./beats.md)
  Used for a music sequence that corresponds to a normal MIDI file. The tempo track defines the number of beats per second and can have multiple tempo events.
- [MusicSequenceType.samples](./samples.md)
  Used for audio samples; a music sequence of this type cannot be saved to a MIDI file. The tempo track contains a single tempo event that specifies an audio sample rate in samples-per-second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/seconds)*