# loudnessResults

**Framework**: MusicUnderstanding  
**Kind**: property

An async sequence that yields loudness analysis results as they become available.

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
nonisolated
var loudnessResults: some Sendable & AsyncSequence<LoudnessResult, any Error> { get }
```

#### Discussion

The sequence ends when the caller receives a `nil` result. You can use the loudness results to update meters real-time in your app. Then use `MusicUnderstanding/SessionResult/` to display peak loudness at the end.

## See Also

- [MusicUnderstandingSession.SessionResult](musicunderstandingsession/sessionresult.md)
  The aggregated results for all analysis types that a music understanding session performs.
- [MusicUnderstandingSession.RangedValue](musicunderstandingsession/rangedvalue.md)
  A structure that pairs a value over a time range.
- [MusicUnderstandingSession.TimedValue](musicunderstandingsession/timedvalue.md)
  A structure that pairs a value with a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/loudnessresults)*