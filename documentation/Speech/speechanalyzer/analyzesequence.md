# analyzeSequence(_:)

**Framework**: Speech  
**Kind**: method

Analyzes an input sequence, returning when the sequence is consumed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func analyzeSequence<InputSequence>(_ inputSequence: InputSequence) async throws -> CMTime? where InputSequence : Sendable, InputSequence : AsyncSequence, InputSequence.Element == AnalyzerInput
```

#### Return Value

The time-code of the last audio sample of the input, or `nil` if the input sequence was empty. You may use this value for the parameter of [`finalizeAndFinish(through:)`](speechanalyzer/finalizeandfinish(through:).md) (or other methods).

#### Discussion

When this method returns, the input sequence will have been consumed, but the last of the audio may still be undergoing analysis. To wait for the analysis to complete, call another method such as [`finalize(through:)`](speechanalyzer/finalize(through:).md) and await its return.

## Parameters

- `inputSequence`: An input sequence to analyze.

## See Also

- [func analyzeSequence(from: AVAudioFile) async throws -> CMTime?](speechanalyzer/analyzesequence(from:).md)
  Analyzes an input sequence created from an audio file, returning when the file has been read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/analyzesequence(_:))*