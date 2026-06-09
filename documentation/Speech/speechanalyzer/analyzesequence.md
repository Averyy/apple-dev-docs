# analyzeSequence(_:)

**Framework**: Speech  
**Kind**: method

Analyzes an input sequence, returning when the sequence terminates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func analyzeSequence<InputSequence>(_ inputSequence: InputSequence) async throws -> CMTime? where InputSequence : Sendable, InputSequence : AsyncSequence, InputSequence.Element == AnalyzerInput
```

#### Return Value

The time-code of the last audio sample that was consumed from this or an earlier input sequence, or `nil` if no audio sample has been consumed. You may use this value for the parameter of [`finalizeAndFinish(through:)`](speechanalyzer/finalizeandfinish(through:).md) (or other methods).

#### Discussion

When this method returns, the last audio consumed from the input sequence may still be undergoing analysis. To wait for the analysis to complete, call another method such as [`finalize(through:)`](speechanalyzer/finalize(through:).md) and await its return.

If you cancel the task executing this method, most input sequences will terminate early, causing this method to return early. The method returns the time-code of the last audio sample that was consumed and does not throw `CancellationError`.

## Parameters

- `inputSequence`: An input sequence to analyze.

## See Also

- [func analyzeSequence(from: AVAudioFile) async throws -> CMTime?](speechanalyzer/analyzesequence(from:).md)
  Analyzes an input sequence created from an audio file, returning when the file has been read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/analyzesequence(_:))*