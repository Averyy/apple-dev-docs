# audioRecorderEncodeErrorDidOccur(_:error:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate that the audio recorder encountered an encoding error during recording.

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
optional func audioRecorderEncodeErrorDidOccur(_ recorder: AVAudioRecorder, error: (any Error)?)
```

## Parameters

- `recorder`: The audio recorder that encountered the encoding error.
- `error`: An object that provides the details of the encoding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderencodeerrordidoccur(_:error:))*