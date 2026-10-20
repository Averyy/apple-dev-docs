# finish(after:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Finishes analysis once input for a given time is consumed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func finish(after: CMTime) async throws
```

#### Discussion

In most cases, you can call [`finalizeAndFinish(through:)`](./finalizeandfinish%28through%29.md) or [`cancelAndFinishNow()`](./cancelandfinishnow%28%29.md) instead. Those methods also finish analysis.

At the return of this method, the modules’ result streams will have ended and the modules will not accept further input from the input sequence. The analyzer will not be able to resume analysis with a different input sequence and will not accept module changes; most methods will do nothing.

Analysis of input up to and including the given time may or may not have been completed. Modules will not publish *additional* results to their streams, but the application can read any results the modules have *already* published. To ensure analysis is completed or skipped before finishing, call [`finalize(through:)`](./finalize%28through%29.md) or [`cancelAnalysis(before:)`](./cancelanalysis%28before%29.md).

You do not need to call this method before releasing this analyzer or its modules.

> **Throws**: `CancellationError` if analysis is finished early before the given input time.

## Parameters

- `after`: An audio time marking the end of the analysis session.

## See Also

### Finishing analysis
- [func cancelAndFinishNow() async](./cancelandfinishnow%28%29.md)
  Finishes analysis immediately.
- [func finalizeAndFinishThroughEndOfInput() async throws](./finalizeandfinishthroughendofinput%28%29.md)
  Finishes analysis after an audio input sequence has been terminated and fully consumed and the modules’ results are finalized.
- [func finalizeAndFinish(through: CMTime) async throws](./finalizeandfinish%28through%29.md)
  Finishes analysis after finalizing results for a given time-code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/finish(after:))*