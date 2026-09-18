# AVAudioSession.DeactivationContext

**Framework**: AVFAudio  
**Kind**: class

An object that describes why and how the audio session deactivated.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
class DeactivationContext
```

## Topics

### Getting the deactivation details
- [var source: AVAudioSession.DeactivationSource](avaudiosession/deactivationcontext/source.md)
  The source of the audio session deactivation.
- [var interruptionContext: AVAudioSession.InterruptionContext?](avaudiosession/deactivationcontext/interruptioncontext.md)
  Context about the interruption that caused deactivation.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [AVAudioSession.DeactivationSource](avaudiosession/deactivationsource.md)
  The source of the audio session deactivation.
- [AVAudioSession.InterruptionContext](avaudiosession/interruptioncontext.md)
  An object that provides context about an audio session interruption.
- [AVAudioSession.ResumptionContext](avaudiosession/resumptioncontext.md)
  An object that provides context when resumption becomes available.
- [AVAudioSession.ResumptionRecommendation](avaudiosession/resumptionrecommendation.md)
  The system’s recommendation on whether to resume playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationcontext)*