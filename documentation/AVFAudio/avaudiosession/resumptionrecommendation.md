# AVAudioSession.ResumptionRecommendation

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVAudioSessionResumptionRecommendation : NSInteger;
```

## Topics

### Creating a resumption recommendation
- [init?(rawValue: Int)](./resumptionrecommendation/init%28rawvalue%29.md)
### Getting the recommendation
- [AVAudioSession.ResumptionRecommendation.shouldResume](./resumptionrecommendation/shouldresume.md)
- [AVAudioSession.ResumptionRecommendation.shouldNotResume](./resumptionrecommendation/shouldnotresume.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting activation context details
- [AVAudioSession.DeactivationContext](./deactivationcontext.md)
  An object that describes why and how the audio session deactivated.
- [AVAudioSession.DeactivationSource](./deactivationsource.md)
  The source of the audio session deactivation.
- [AVAudioSession.InterruptionContext](./interruptioncontext.md)
  An object that provides context about an audio session interruption.
- [AVAudioSession.ResumptionContext](./resumptioncontext.md)
  An object that provides context when resumption becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/resumptionrecommendation)*