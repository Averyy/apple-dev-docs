# finalizeAndFinishThroughEndOfInput()

**Framework**: Speech  
**Kind**: method

Finishes analysis after an audio input sequence has been fully consumed and its results are finalized.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func finalizeAndFinishThroughEndOfInput() async throws
```

#### Discussion

This method waits until the input sequence has terminated, then finalizes like [`finalize(through:)`](speechanalyzer/finalize(through:).md) and finishes analysis like [`finish(after:)`](speechanalyzer/finish(after:).md).

If the input sequence is replaced using one of the `start` methods, this method continues waiting for the replacement input sequence to terminate.

> **Note**: `CancellationError` if analysis is finished early before the end of input

## See Also

- [func cancelAndFinishNow() async](speechanalyzer/cancelandfinishnow.md)
  Finishes analysis immediately.
- [func finalizeAndFinish(through: CMTime) async throws](speechanalyzer/finalizeandfinish(through:).md)
  Finishes analysis after finalizing results for a given time-code.
- [func finish(after: CMTime) async throws](speechanalyzer/finish(after:).md)
  Finishes analysis once input for a given time is consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/finalizeandfinishthroughendofinput())*