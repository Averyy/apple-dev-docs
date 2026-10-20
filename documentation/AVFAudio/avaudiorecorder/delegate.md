# delegate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (weak, nullable) id<AVAudioRecorderDelegate> delegate;
```

## See Also

### Responding to recorder events
- [protocol AVAudioRecorderDelegate](../avaudiorecorderdelegate.md)
  A protocol that defines the methods to respond to audio recording events and encoding errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/delegate)*