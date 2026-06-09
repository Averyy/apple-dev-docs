# interruptionContext

**Framework**: AVFAudio  
**Kind**: property

Context about the interruption that caused deactivation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var interruptionContext: AVAudioSession.InterruptionContext? { get }
```

#### Discussion

This property is only present when the session was interrupted by another application.

## See Also

- [var source: AVAudioSession.DeactivationSource](avaudiosession/deactivationcontext/source.md)
  The source of the audio session deactivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationcontext/interruptioncontext)*