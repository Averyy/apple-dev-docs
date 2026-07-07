# InstrumentActivityResult

**Framework**: Music Understanding  
**Kind**: struct

A structure containing the activity levels and detected time ranges for instruments in a song.

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
struct InstrumentActivityResult
```

#### Overview

The [`activity`](instrumentactivityresult/activity.md) property provides a continuous signal for each instrument. The values range from `0.0`, which indicates the instrument isn’t  present, to `1.0`, which indicates the instrument is fully active. The [`ranges`](instrumentactivityresult/ranges.md) property provides discrete time windows during which the framework detected each instrument. Use both properties together to determine when an instrument is present and how prominently it features at each moment.

## Topics

### Structures
- [InstrumentActivityResult.Instrument](instrumentactivityresult/instrument.md)
  A type that identifies a specific instrument category.
### Instance Properties
- [let activity: [InstrumentActivityResult.Instrument : [MusicUnderstandingSession.TimedValue<Float>]]](instrumentactivityresult/activity.md)
  The activity level of each instrument over time, as values from 0.0 to 1.0.
- [let ranges: [InstrumentActivityResult.Instrument : [CMTimeRange]]](instrumentactivityresult/ranges.md)
  The time ranges during which the framework detects each instrument.

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
- [struct StructureResult](structureresult.md)
  A song’s structural boundary information, including sections, segments, and phrases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/instrumentactivityresult)*