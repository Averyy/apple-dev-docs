# finish(after:)

**Framework**: Speech  
**Kind**: method

Finishes analysis once input for a given time is consumed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func finish(after: CMTime) async throws
```

#### Discussion

In most cases, you can call [`finalizeAndFinish(through:)`](speechanalyzer/finalizeandfinish(through:).md) or [`cancelAndFinishNow()`](speechanalyzer/cancelandfinishnow().md) instead. Those methods also finish analysis.

At the return of this method, the modules’ result streams will have ended and the modules will not accept further input from the input sequence. The analyzer will not be able to resume analysis with a different input sequence and will not accept module changes; most methods will do nothing.

Analysis of input up to and including the given time may or may not have been completed. Modules will not publish  results to their streams, but the application can read any results the modules have  published. To ensure analysis is completed or skipped before finishing, call [`finalize(through:)`](speechanalyzer/finalize(through:).md) or [`cancelAnalysis(before:)`](speechanalyzer/cancelanalysis(before:).md).

You do not need to call this method before releasing this analyzer or its modules.

> **Note**: `CancellationError` if analysis is finished early before the given input time.

## Parameters

- `after`: An audio time marking the end of the analysis session.

## See Also

- [func cancelAndFinishNow() async](speechanalyzer/cancelandfinishnow.md)
  Finishes analysis immediately.
- [func finalizeAndFinishThroughEndOfInput() async throws](speechanalyzer/finalizeandfinishthroughendofinput.md)
  Finishes analysis after an audio input sequence has been fully consumed and its results are finalized.
- [func finalizeAndFinish(through: CMTime) async throws](speechanalyzer/finalizeandfinish(through:).md)
  Finishes analysis after finalizing results for a given time-code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/finish(after:))*