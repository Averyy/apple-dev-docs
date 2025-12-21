# cancelAndFinishNow()

**Framework**: Speech  
**Kind**: method

Finishes analysis immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func cancelAndFinishNow() async
```

#### Discussion

This method cancels all pending work and then finishes analysis. It works similarly to calling [`cancelAnalysis(before:)`](speechanalyzer/cancelanalysis(before:).md) and then [`finish(after:)`](speechanalyzer/finish(after:).md), but unlike `finish(after:)`, this method is able to finish analysis prior to any input. The post-conditions for this method are identical to `finish(after:)`.

You do not need to call this method before releasing this analyzer or its modules.

## See Also

- [func finalizeAndFinishThroughEndOfInput() async throws](speechanalyzer/finalizeandfinishthroughendofinput.md)
  Finishes analysis after an audio input sequence has been fully consumed and its results are finalized.
- [func finalizeAndFinish(through: CMTime) async throws](speechanalyzer/finalizeandfinish(through:).md)
  Finishes analysis after finalizing results for a given time-code.
- [func finish(after: CMTime) async throws](speechanalyzer/finish(after:).md)
  Finishes analysis once input for a given time is consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/cancelandfinishnow())*