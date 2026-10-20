# AVAudioSession.DeactivationContext

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioSessionDeactivationContext : NSObject
```

## Mentions

- [Handling audio interruptions](../handling-audio-interruptions.md)

## Topics

### Getting the deactivation details
- [var source: AVAudioSession.DeactivationSource](./deactivationcontext/source.md)
  The source of the audio session deactivation.
- [var interruptionContext: AVAudioSession.InterruptionContext?](./deactivationcontext/interruptioncontext.md)
  Context about the interruption that caused deactivation.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting activation context details
- [AVAudioSession.DeactivationSource](./deactivationsource.md)
  The source of the audio session deactivation.
- [AVAudioSession.InterruptionContext](./interruptioncontext.md)
  An object that provides context about an audio session interruption.
- [AVAudioSession.ResumptionContext](./resumptioncontext.md)
  An object that provides context when resumption becomes available.
- [AVAudioSession.ResumptionRecommendation](./resumptionrecommendation.md)
  The system’s recommendation on whether to resume playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationcontext)*