# RhythmResult

**Framework**: MusicUnderstanding  
**Kind**: struct

A structure that describes a song’s rhythm results in terms of beats, bars, and beats per minute (BPM).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct RhythmResult
```

#### Overview

- **Bars**: A group of beats, typically containing 2-4 beats depending on the song’s time signature.
- **Beats**: The basic, recurrent pulse of a song.
- **Beats Per Minute (BPM)**: The tempo of the song, measuring how many beats occur in one minute.

## Topics

### Types of rhythm results
- [let bars: [CMTime]](rhythmresult/bars.md)
  The start time of each bar. A bar is a musical unit typically containing several beats.
- [let beats: [CMTime]](rhythmresult/beats.md)
  The timestamp of each detected beat.
- [let beatsPerMinute: Float?](rhythmresult/beatsperminute.md)
  The tempo of the song in beats per minute.
### Instance Properties
- [var debugDescription: String](rhythmresult/debugdescription.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MusicUnderstandingSession.SessionResult](musicunderstandingsession/sessionresult.md)
  The aggregated results for all analysis types that a music understanding session performs.
- [struct KeyResult](keyresult.md)
  A value describing the musical key detected over a time range.
- [struct LoudnessResult](loudnessresult.md)
  A structure that contains perceptual loudness measurements for a song, including integrated, momentary, short-term, and peak values.
- [struct PaceResult](paceresult.md)
  A pace analysis results for the song.
- [struct StructureResult](structureresult.md)
  A song’s structural boundary information, including sections, segments, and phrases.
- [struct InstrumentActivityResult](instrumentactivityresult.md)
  A structure containing the activity levels and detected time ranges for instruments in a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/rhythmresult)*