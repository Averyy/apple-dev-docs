# audioRecorderDidFinishRecording(_:successfully:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when recording stops or finishes due to reaching its time limit.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool)
```

#### Discussion

The system doesn’t call this method if the recorder stops due to an interruption.

## Parameters

- `recorder`: The audio recorder that finished recording.
- `flag`: A Boolean value that indicates whether the recording stopped successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderdidfinishrecording(_:successfully:))*