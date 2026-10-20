# cancelAndFinishNow()

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Finishes analysis immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func cancelAndFinishNow() async
```

#### Discussion

This method cancels all pending work and then finishes analysis. It works similarly to calling [`cancelAnalysis(before:)`](./cancelanalysis%28before%29.md) and then [`finish(after:)`](./finish%28after%29.md), but unlike `finish(after:)`, this method is able to finish analysis prior to any input. The post-conditions for this method are identical to `finish(after:)`.

You do not need to call this method before releasing this analyzer or its modules.

## See Also

### Finishing analysis
- [func finalizeAndFinishThroughEndOfInput() async throws](./finalizeandfinishthroughendofinput%28%29.md)
  Finishes analysis after an audio input sequence has been terminated and fully consumed and the modules’ results are finalized.
- [func finalizeAndFinish(through: CMTime) async throws](./finalizeandfinish%28through%29.md)
  Finishes analysis after finalizing results for a given time-code.
- [func finish(after: CMTime) async throws](./finish%28after%29.md)
  Finishes analysis once input for a given time is consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/cancelandfinishnow())*