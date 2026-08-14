# PaceResult

**Framework**: Music Understanding  
**Kind**: struct

A pace analysis results for the song.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct PaceResult
```

#### Overview

The results indicate the energy and momentum of the music over time. Parts of a song that feel faster or more energetic have a higher value compared to slower or less energetic parts of a song. These values represent a perceptual events-per-minute rate. The perceptual events-per-minute rate allows you to synchronize behaviors with the music’s changing energy, independent of the fixed tempo. For example, a song with a high BPM might yield a lower `Pace` value during a sparse breakdown.

## Topics

### Getting the range
- [let ranges: [MusicUnderstandingSession.RangedValue<Double>]](paceresult/ranges.md)
  The pace for a range of a song.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [MusicUnderstandingSession.SessionResult](musicunderstandingsession/sessionresult.md)
  The aggregated results for all analysis types that a music understanding session performs.
- [struct RhythmResult](rhythmresult.md)
  A structure that describes a song’s rhythm results in terms of beats, bars, and beats per minute (BPM).
- [struct KeyResult](keyresult.md)
  A value describing the musical key detected over a time range.
- [struct LoudnessResult](loudnessresult.md)
  A structure that contains perceptual loudness measurements for a song, including integrated, momentary, short-term, and peak values.
- [struct StructureResult](structureresult.md)
  A song’s structural boundary information, including sections, segments, and phrases.
- [struct InstrumentActivityResult](instrumentactivityresult.md)
  A structure containing the activity levels and detected time ranges for instruments in a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/paceresult)*