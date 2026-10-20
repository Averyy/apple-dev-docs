# finalizeAndFinishThroughEndOfInput()

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Finishes analysis after an audio input sequence has been terminated and fully consumed and the modules’ results are finalized.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func finalizeAndFinishThroughEndOfInput() async throws
```

#### Discussion

This method waits until the input sequence has been terminated and fully consumed, then finalizes like [`finalize(through:)`](./finalize%28through%29.md) and finishes analysis like [`finish(after:)`](./finish%28after%29.md).

If there is no input sequence, this method waits until there is an input sequence and the sequence terminates. If the input sequence is replaced using one of the `start` methods, this method continues waiting for the replacement input sequence to terminate.

This method is primarily useful for autonomous analysis started via one of the `start` methods or a similar initializer.

> **Throws**: `CancellationError` if analysis is finished early before the end of input

## See Also

### Finishing analysis
- [func cancelAndFinishNow() async](./cancelandfinishnow%28%29.md)
  Finishes analysis immediately.
- [func finalizeAndFinish(through: CMTime) async throws](./finalizeandfinish%28through%29.md)
  Finishes analysis after finalizing results for a given time-code.
- [func finish(after: CMTime) async throws](./finish%28after%29.md)
  Finishes analysis once input for a given time is consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/finalizeandfinishthroughendofinput())*