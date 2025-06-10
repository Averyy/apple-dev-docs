# finalizeAndFinish(through:)

**Framework**: Speech  
**Kind**: method

Finishes analysis after finalizing results for a given time-code.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func finalizeAndFinish(through: CMTime) async throws
```

#### Discussion

This method finalizes like [`finalize(through:)`](speechanalyzer/finalize(through:).md) and finishes analysis like [`finish(after:)`](speechanalyzer/finish(after:).md).

> **Note**: Various errors including `CancellationError` if analysis is finished early before the given input time.

## Parameters

- `through`: A time-code of the last audio sample that you want to analyze.

## See Also

- [func cancelAndFinishNow() async](speechanalyzer/cancelandfinishnow.md)
  Finishes analysis immediately.
- [func finalizeAndFinishThroughEndOfInput() async throws](speechanalyzer/finalizeandfinishthroughendofinput.md)
  Finishes analysis after an audio input sequence has been fully consumed and its results are finalized.
- [func finish(after: CMTime) async throws](speechanalyzer/finish(after:).md)
  Finishes analysis once input for a given time is consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/finalizeandfinish(through:))*