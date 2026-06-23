# Music Understanding

**Framework**: Music Understanding  
**Kind**: module

Analyze audio content and extract music information.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

#### Overview

Use the Music Understanding framework to analyze your audio content and receive information like the rhythm, pace, loudness, key, and instrument activity.

![Framework overview art showing a music note and audio stream.](https://docs-assets.developer.apple.com/published/0cae6e395374de96392a2f2e2ac9295c/music-understanding-hero%402x.png)

You create a [`MusicUnderstandingSession`](musicunderstandingsession.md), specify which analysis to run, and receive the results. When complete, the framework presents the results in a single aggregate from [`MusicUnderstandingSession.SessionResult`](musicunderstandingsession/sessionresult.md), or as a livestream of partial results. You can provide audio from an `AVAsset` for file-based analysis of a complete audio track, or an `AsyncSequence` of `AVReadOnlyAudioPCMBuffer` for a stream analysis of audio buffers.

Some analyses also support incremental delivery through async sequences on the session. Use [`loudnessResults`](musicunderstandingsession/loudnessresults.md) to receive values intermittently while analysis is in-progress. Call [`cancel()`](musicunderstandingsession/cancel().md) to stop an in-progress analysis.

The framework returns each analysis type as a dedicated result structure, giving you detailed, time-stamped data for the requested analyses:

- **Rhythm**: Beat positions, bar boundaries, and tempo in beats per minute (BPM).
- **Key**: Musical key (tonic and mode) detected over time ranges.
- **Loudness**: Perceptual loudness measurements following the ITU-R BS.1770 standard, including integrated, short-term, momentary, and peak values.
- **Pace**: Perceptual energy and momentum expressed as an events-per-minute rate, independent of fixed tempo.
- **Structure**: Song-level organization in terms of sections, segments, and phrases.

## Topics

### Essentials
- [Creating visuals with Music Understanding analysis results](create-visuals-using-musicunderstanding-analysis-results.md)
  Create a multiplatform app that presents analysis results from the Music Understanding framework.
### Audio analysis
- [actor MusicUnderstandingSession](musicunderstandingsession.md)
  An object that performs music analysis on an audio source and provides the results.
### Content results
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
- [struct InstrumentActivityResult](instrumentactivityresult.md)
  A structure containing the activity levels and detected time ranges for instruments in a song.
### Support types
- [MusicUnderstandingSession.TimedValue](musicunderstandingsession/timedvalue.md)
  A structure that pairs a value with a time.
- [MusicUnderstandingSession.RangedValue](musicunderstandingsession/rangedvalue.md)
  A structure that pairs a value over a time range.
- [struct AnalysisType](analysistype.md)
  The analysis type for each session.
### Errors
- [enum MusicUnderstandingError](musicunderstandingerror.md)
  An error that occurs during a music understanding session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MusicUnderstanding)*