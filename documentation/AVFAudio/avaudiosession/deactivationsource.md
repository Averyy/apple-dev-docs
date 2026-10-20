# AVAudioSession.DeactivationSource

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVAudioSessionDeactivationSource : NSInteger;
```

## Topics

### Creating a deactivation source
- [init?(rawValue: Int)](./deactivationsource/init%28rawvalue%29.md)
### Getting the source
- [AVAudioSession.DeactivationSource.app](./deactivationsource/app.md)
- [AVAudioSession.DeactivationSource.system](./deactivationsource/system.md)

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
- [AVAudioSession.InterruptionContext](./interruptioncontext.md)
  An object that provides context about an audio session interruption.
- [AVAudioSession.ResumptionContext](./resumptioncontext.md)
  An object that provides context when resumption becomes available.
- [AVAudioSession.ResumptionRecommendation](./resumptionrecommendation.md)
  The system’s recommendation on whether to resume playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationsource)*