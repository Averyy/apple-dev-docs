# KeyResult

**Framework**: Music Understanding  
**Kind**: struct

A value describing the musical key detected over a time range.

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
struct KeyResult
```

#### Overview

A key is the central note that organizes a piece of music. The tonic can be any of the supported enharmonic spellings: A, A♭, A♯, B♭, B, C, C♯, D♭, D, D♯, E♭, E, F, F♯, G, G♭, or G♯. The framework represents the enharmonic equivalents as distinct cases to preserve the original spelling.

## Topics

### Getting key result ranges
- [let ranges: [MusicUnderstandingSession.RangedValue<KeyResult.KeySignature>]](keyresult/ranges.md)
  The detected key for each time range.
### Getting the mode of the musical key
- [let mode: KeyResult.Mode](keyresult/keysignature/mode.md)
  The mode of the musical key.
### Getting the notes of a key
- [KeyResult.KeySignature](keyresult/keysignature.md)
  The set of sharp and flat symbols for the notes.
- [let tonic: KeyResult.Tonic](keyresult/keysignature/tonic.md)
  The root note of the musical key.
### Enumerations
- [KeyResult.Mode](keyresult/mode.md)
  The mode of a musical key.
- [KeyResult.Tonic](keyresult/tonic.md)
  The root note of a musical key.

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
- [struct LoudnessResult](loudnessresult.md)
  A structure that contains perceptual loudness measurements for a song, including integrated, momentary, short-term, and peak values.
- [struct PaceResult](paceresult.md)
  A pace analysis results for the song.
- [struct StructureResult](structureresult.md)
  A song’s structural boundary information, including sections, segments, and phrases.
- [struct InstrumentActivityResult](instrumentactivityresult.md)
  A structure containing the activity levels and detected time ranges for instruments in a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/keyresult)*