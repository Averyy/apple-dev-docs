# MusicUnderstandingSession.SessionResult

**Framework**: Music Understanding  
**Kind**: struct  
**Role**: Structure

The aggregated results for all analysis types that a music understanding session performs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct SessionResult
```

## Overview

Each property corresponds to one analysis type that the session can perform: the instrument activity, key, loudness, rhythm, pace, and structure. A property is nil if the session wasn’t configured to perform that analysis. Access a session result after the session finishes processing audio to retrieve the data for each configured type.

## Topics

### Getting music understanding session results
- [let instrumentActivity: InstrumentActivityResult?](./sessionresult/instrumentactivity.md)
  The aggregated instrument activity results, identifying which instruments are present and when they’re active.
- [let key: KeyResult?](./sessionresult/key.md)
  The aggregated key results, identifying the central note (tonic) and mode around which a piece of music is organized.
- [let loudness: LoudnessResult?](./sessionresult/loudness.md)
  The aggregated loudness results, providing information about volume levels throughout the audio.
- [let pace: PaceResult?](./sessionresult/pace.md)
  The aggregated pace results, describing the energy and momentum variations over time.
- [let rhythm: RhythmResult?](./sessionresult/rhythm.md)
  The aggregated rhythm results, including detected beats, bars, and BPM.
- [let structure: StructureResult?](./sessionresult/structure.md)
  The aggregated structure results, identifying musical sections and their boundaries.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Content results
- [struct RhythmResult](../rhythmresult.md)
  A structure that describes a song’s rhythm results in terms of beats, bars, and beats per minute (BPM).
- [struct KeyResult](../keyresult.md)
  A value describing the musical key detected over a time range.
- [struct LoudnessResult](../loudnessresult.md)
  A structure that contains perceptual loudness measurements for a song, including integrated, momentary, short-term, and peak values.
- [struct PaceResult](../paceresult.md)
  A pace analysis results for the song.
- [struct StructureResult](../structureresult.md)
  A song’s structural boundary information, including sections, segments, and phrases.
- [struct InstrumentActivityResult](../instrumentactivityresult.md)
  A structure containing the activity levels and detected time ranges for instruments in a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/sessionresult)*