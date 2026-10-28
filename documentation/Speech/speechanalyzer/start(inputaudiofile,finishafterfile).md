# start(inputAudioFile:finishAfterFile:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Starts analysis of an input sequence created from an audio file and returns immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func start(inputAudioFile audioFile: AVAudioFile, finishAfterFile: Bool = false) async throws
```

## Discussion

This method stops the autonomous analysis of the previous input sequence. Any audio that hasn’t been consumed will be ignored but audio that has been consumed will continue to be analyzed. To ensure the previous sequence’s input is fully consumed, call [`finalize(through:)`](./finalize%28through%29.md) first.

## Parameters

- `audioFile`: An AVAudioFile opened for reading.
- `finishAfterFile`: If `true`, the analysis will automatically finish after the audio file has been fully processed. Equivalent to calling [`finalizeAndFinishThroughEndOfInput()`](./finalizeandfinishthroughendofinput%28%29.md).

## See Also

### Performing autonomous analysis
- [func start<InputSequence>(inputSequence: InputSequence) async throws](./start%28inputsequence%29.md)
  Starts analysis of an input sequence and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/start(inputaudiofile:finishafterfile:))*