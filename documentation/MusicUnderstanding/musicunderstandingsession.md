# MusicUnderstandingSession

**Framework**: Music Understanding  
**Kind**: class  
**Role**: Class

An object that performs music analysis on an audio source and provides the results.

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
actor MusicUnderstandingSession
```

## Topics

### Creating a session
- [convenience init<Provider>(audioProvider: Provider)](./musicunderstandingsession/init%28audioprovider%29.md)
  Creates a music understanding session that accepts streaming audio buffers.
- [convenience init(asset: any AVAsset & Sendable) async throws](./musicunderstandingsession/init%28asset%29.md)
  Creates a music understanding session from an audio asset.
### Performing an analysis
- [func analyze() async throws -> MusicUnderstandingSession.SessionResult](./musicunderstandingsession/analyze%28%29.md)
  Performs all available analyses on the session’s audio source.
- [func analyze(for: Set<AnalysisType>) async throws -> MusicUnderstandingSession.SessionResult](./musicunderstandingsession/analyze%28for%29.md)
  Performs the specified analyses on the session’s audio source.
### Getting analysis results
- [MusicUnderstandingSession.SessionResult](./musicunderstandingsession/sessionresult.md)
  The aggregated results for all analysis types that a music understanding session performs.
- [var loudnessResults: some Sendable & AsyncSequence<LoudnessResult, any Error>](./musicunderstandingsession/loudnessresults.md)
  An async sequence that yields loudness analysis results as they become available.
- [MusicUnderstandingSession.RangedValue](./musicunderstandingsession/rangedvalue.md)
  A structure that pairs a value over a time range.
- [MusicUnderstandingSession.TimedValue](./musicunderstandingsession/timedvalue.md)
  A structure that pairs a value with a time.
### Cancelling a session
- [func cancel() async](./musicunderstandingsession/cancel%28%29.md)
  Cancels any ongoing analysis.

## Relationships

### Conforms To
- [Actor](../Swift/actor.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession)*