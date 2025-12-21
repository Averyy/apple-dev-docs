# start(inputAudioFile:finishAfterFile:)

**Framework**: Speech  
**Kind**: method

Starts analysis of an input sequence created from an audio file and returns immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func start(inputAudioFile audioFile: AVAudioFile, finishAfterFile: Bool = false) async throws
```

#### Discussion

This method stops the autonomous analysis of the previous input sequence. To ensure the previous sequence’s input is fully consumed, call [`finalize(through:)`](speechanalyzer/finalize(through:).md) first.

## Parameters

- `audioFile`: An AVAudioFile opened for reading.
- `finishAfterFile`: If  , the analysis will automatically finish after the audio file has been fully processed. Equivalent to calling  .

## See Also

- [func start<InputSequence>(inputSequence: InputSequence) async throws](speechanalyzer/start(inputsequence:).md)
  Starts analysis of an input sequence and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/start(inputaudiofile:finishafterfile:))*