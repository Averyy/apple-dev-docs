# interruptionContext

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Context about the interruption that caused deactivation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var interruptionContext: AVAudioSession.InterruptionContext? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVAudioSessionInterruptionContext * interruptionContext;
```

## Mentions

- [Handling audio interruptions](../../handling-audio-interruptions.md)

## Discussion

This property is only present when the session was interrupted by another application.

## See Also

### Getting the deactivation details
- [var source: AVAudioSession.DeactivationSource](./source.md)
  The source of the audio session deactivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationcontext/interruptioncontext)*