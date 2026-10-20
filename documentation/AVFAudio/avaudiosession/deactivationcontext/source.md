# source

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The source of the audio session deactivation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var source: AVAudioSession.DeactivationSource { get }
```

```objc
@property (nonatomic, readonly) AVAudioSessionDeactivationSource source;
```

## Mentions

- [Handling audio interruptions](../../handling-audio-interruptions.md)

## See Also

### Getting the deactivation details
- [var interruptionContext: AVAudioSession.InterruptionContext?](./interruptioncontext.md)
  Context about the interruption that caused deactivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationcontext/source)*