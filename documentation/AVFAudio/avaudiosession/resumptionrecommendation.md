# AVAudioSession.ResumptionRecommendation

**Framework**: AVFAudio  
**Kind**: enum

The system’s recommendation on whether to resume playback.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum ResumptionRecommendation
```

## Topics

### Creating a resumption recommendation
- [init?(rawValue: Int)](avaudiosession/resumptionrecommendation/init(rawvalue:).md)
### Getting the recommendation
- [AVAudioSession.ResumptionRecommendation.shouldResume](avaudiosession/resumptionrecommendation/shouldresume.md)
- [AVAudioSession.ResumptionRecommendation.shouldNotResume](avaudiosession/resumptionrecommendation/shouldnotresume.md)

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
- [AVAudioSession.DeactivationSource](avaudiosession/deactivationsource.md)
  The source of the audio session deactivation.
- [AVAudioSession.InterruptionContext](avaudiosession/interruptioncontext.md)
  An object that provides context about an audio session interruption.
- [AVAudioSession.ResumptionContext](avaudiosession/resumptioncontext.md)
  An object that provides context when resumption becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/resumptionrecommendation)*