# start(inputSequence:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Starts analysis of an input sequence and returns immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func start<InputSequence>(inputSequence: InputSequence) async throws where InputSequence : Sendable, InputSequence : AsyncSequence, InputSequence.Element == AnalyzerInput
```

## Discussion

This method stops the autonomous analysis of the previous input sequence. Any audio that hasn’t been consumed will be ignored but audio that has been consumed will continue to be analyzed. To ensure the previous sequence’s input is fully consumed, call [`finalize(through:)`](./finalize%28through%29.md) first.

The previous input sequence may be rendered inoperable depending on its implementation.

## Parameters

- `inputSequence`: A new input sequence.

## See Also

### Performing autonomous analysis
- [func start(inputAudioFile: AVAudioFile, finishAfterFile: Bool) async throws](./start%28inputaudiofile,finishafterfile%29.md)
  Starts analysis of an input sequence created from an audio file and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/start(inputsequence:))*