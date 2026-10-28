# analyzeSequence(from:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Analyzes an input sequence created from an audio file, returning when the file has been read.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func analyzeSequence(from audioFile: AVAudioFile) async throws -> CMTime?
```

## Return Value

The time-code of the last audio sample of the input, or `nil` if the file was empty. You may use this value for the parameter of [`finalizeAndFinish(through:)`](./finalizeandfinish%28through%29.md) (or other methods).

## Discussion

When this method returns, the file will have been read, but the last of the audio may still be undergoing analysis. To wait for the analysis to complete, call another method such as [`finalize(through:)`](./finalize%28through%29.md) and await its return.

## Parameters

- `audioFile`: An `AVAudioFile` opened for reading.

## See Also

### Performing analysis
- [func analyzeSequence<InputSequence>(InputSequence) async throws -> CMTime?](./analyzesequence%28_%29.md)
  Analyzes an input sequence, returning when the sequence terminates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/analyzesequence(from:))*