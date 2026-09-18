# AVAudioSession.DeactivationSource

**Framework**: AVFAudio  
**Kind**: enum

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
enum DeactivationSource
```

## Topics

### Creating a deactivation source
- [init?(rawValue: Int)](avaudiosession/deactivationsource/init(rawvalue:).md)
### Getting the source
- [AVAudioSession.DeactivationSource.app](avaudiosession/deactivationsource/app.md)
- [AVAudioSession.DeactivationSource.system](avaudiosession/deactivationsource/system.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [AVAudioSession.DeactivationContext](avaudiosession/deactivationcontext.md)
  An object that describes why and how the audio session deactivated.
- [AVAudioSession.InterruptionContext](avaudiosession/interruptioncontext.md)
  An object that provides context about an audio session interruption.
- [AVAudioSession.ResumptionContext](avaudiosession/resumptioncontext.md)
  An object that provides context when resumption becomes available.
- [AVAudioSession.ResumptionRecommendation](avaudiosession/resumptionrecommendation.md)
  The system’s recommendation on whether to resume playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationsource)*