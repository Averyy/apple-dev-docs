# analyzeSequence(from:)

**Framework**: Speech  
**Kind**: method

Analyzes an input sequence created from an audio file, returning when the file has been read.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func analyzeSequence(from audioFile: AVAudioFile) async throws -> CMTime?
```

#### Return Value

The time-code of the last audio sample of the input, or `nil` if the file was empty. You may use this value for the parameter of [`finalizeAndFinish(through:)`](speechanalyzer/finalizeandfinish(through:).md) (or other methods).

#### Discussion

When this method returns, the input sequence will have been consumed, but the last of the audio may still be undergoing analysis. To wait for the analysis to complete, call another method such as [`finalize(through:)`](speechanalyzer/finalize(through:).md) and await its return.

## Parameters

- `audioFile`: An AVAudioFile opened for reading.

## See Also

- [func analyzeSequence<InputSequence>(InputSequence) async throws -> CMTime?](speechanalyzer/analyzesequence(_:).md)
  Analyzes an input sequence, returning when the sequence is consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/analyzesequence(from:))*