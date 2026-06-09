# StructureResult

**Framework**: MusicUnderstanding  
**Kind**: struct

A song’s structural boundary information, including sections, segments, and phrases.

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
struct StructureResult
```

#### Overview

The `StructureResult` describes a song’s structure in terms of sections, segments and phrases. A section corresponds to a distinct part of a song, such as an intro, verse, or chorus. A section consists of one or more segments, and each segment consists of one or more phrases.

## Topics

### Instance Properties
- [var debugDescription: String](structureresult/debugdescription.md)
- [let phrases: [CMTimeRange]](structureresult/phrases.md)
  The time range of each phrase in the song.
- [let sections: [CMTimeRange]](structureresult/sections.md)
  The time ranges of each section in the song.
- [let segments: [CMTimeRange]](structureresult/segments.md)
  The time range of each segment in the song.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MusicUnderstandingSession.SessionResult](musicunderstandingsession/sessionresult.md)
  The aggregated results for all analysis types that a music understanding session performs.
- [struct RhythmResult](rhythmresult.md)
  A structure that describes a song’s rhythm results in terms of beats, bars, and beats per minute (BPM).
- [struct KeyResult](keyresult.md)
  A value describing the musical key detected over a time range.
- [struct LoudnessResult](loudnessresult.md)
  A structure that contains perceptual loudness measurements for a song, including integrated, momentary, short-term, and peak values.
- [struct PaceResult](paceresult.md)
  A pace analysis results for the song.
- [struct InstrumentActivityResult](instrumentactivityresult.md)
  A structure containing the activity levels and detected time ranges for instruments in a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/structureresult)*