# start(inputSequence:)

**Framework**: Speech  
**Kind**: method

Starts analysis of an input sequence and returns immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func start<InputSequence>(inputSequence: InputSequence) async throws where InputSequence : Sendable, InputSequence : AsyncSequence, InputSequence.Element == AnalyzerInput
```

#### Discussion

This method stops the autonomous analysis of the previous input sequence. To ensure the previous sequence’s input is fully consumed, call [`finalize(through:)`](speechanalyzer/finalize(through:).md) first.

The previous input sequence may be rendered inoperable depending on its implementation.

## Parameters

- `inputSequence`: A new input sequence.

## See Also

- [func start(inputAudioFile: AVAudioFile, finishAfterFile: Bool) async throws](speechanalyzer/start(inputaudiofile:finishafterfile:).md)
  Starts analysis of an input sequence created from an audio file and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/start(inputsequence:))*