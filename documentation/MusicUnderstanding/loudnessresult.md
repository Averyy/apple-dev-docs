# LoudnessResult

**Framework**: MusicUnderstanding  
**Kind**: struct

A structure that contains perceptual loudness measurements for a song, including integrated, momentary, short-term, and peak values.

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
struct LoudnessResult
```

#### Overview

The `LoudnessResult` delivers perceptual loudness measurements that align with human hearing perception, using the Loudness K-weighted Full Scale (LUFS) standard defined in ITU-R BS.1770.

The results contain time-based measurements, including integrated loudness, short-term loudness, momentary loudness, and peak amplitude.

When used in `SessionResult`, a single `LoudnessResult` contains all analysis values for the entire song, with `momentary` and `shortTerm` arrays containing the complete set of measurements across the song’s duration.

When used in the streaming `loudnessResults` context, the framework delivers multiple results progressively during analysis. Each result’s [`momentary`](loudnessresult/momentary.md) and [`shortTerm`](loudnessresult/shortterm.md) arrays contain only one value representing the measurement at that point in time.

## Topics

### Getting loudness results
- [let integrated: MusicUnderstandingSession.TimedValue<Float>](loudnessresult/integrated.md)
  The integrated loudness of the song, measured in LUFS over its full duration.
- [let momentary: [MusicUnderstandingSession.TimedValue<Float>]](loudnessresult/momentary.md)
  An array of momentary loudness measurements sampled across the song in LUFS.
- [let peak: MusicUnderstandingSession.TimedValue<Float>](loudnessresult/peak.md)
  The peak amplitude of the song in decibels (dB).
- [let shortTerm: [MusicUnderstandingSession.TimedValue<Float>]](loudnessresult/shortterm.md)
  An array of short-term loudness measurements sampled across the song in LUFS.
### Instance Properties
- [var debugDescription: String](loudnessresult/debugdescription.md)

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
- [struct PaceResult](paceresult.md)
  A pace analysis results for the song.
- [struct StructureResult](structureresult.md)
  A song’s structural boundary information, including sections, segments, and phrases.
- [struct InstrumentActivityResult](instrumentactivityresult.md)
  A structure containing the activity levels and detected time ranges for instruments in a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/loudnessresult)*