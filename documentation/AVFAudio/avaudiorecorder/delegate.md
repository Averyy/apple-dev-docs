# delegate

**Framework**: AVFAudio  
**Kind**: property

The delegate object for the audio recorder.

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
weak var delegate: (any AVAudioRecorderDelegate)? { get set }
```

## See Also

- [protocol AVAudioRecorderDelegate](avaudiorecorderdelegate.md)
  A protocol that defines the methods to respond to audio recording events and encoding errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/delegate)*