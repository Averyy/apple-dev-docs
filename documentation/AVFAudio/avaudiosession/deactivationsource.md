# AVAudioSession.DeactivationSource

**Framework**: AVFAudio  
**Kind**: enum

The source of the audio session deactivation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum DeactivationSource
```

## Topics

### Getting the source
- [AVAudioSession.DeactivationSource.app](avaudiosession/deactivationsource/app.md)
- [AVAudioSession.DeactivationSource.system](avaudiosession/deactivationsource/system.md)
### Creating a deactivation source
- [init?(rawValue: Int)](avaudiosession/deactivationsource/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class let didBecomeActiveNotification: NSNotification.Name](avaudiosession/didbecomeactivenotification.md)
  Notification sent when the audio session becomes active.
- [class let didBecomeInactiveNotification: NSNotification.Name](avaudiosession/didbecomeinactivenotification.md)
  Notification sent when the audio session becomes inactive.
- [class let resumptionRecommendationNotification: NSNotification.Name](avaudiosession/resumptionrecommendationnotification.md)
  Notification sent when the system provides a resumption recommendation.
- [class let deactivationContextKey: String](avaudiosession/deactivationcontextkey.md)
  Keys for [`didBecomeInactiveNotification`](avaudiosession/didbecomeinactivenotification.md) Value is an [`AVAudioSession.DeactivationContext`](avaudiosession/deactivationcontext.md) object describing the deactivation.
- [class let resumptionContextKey: String](avaudiosession/resumptioncontextkey.md)
  Keys for [`resumptionRecommendationNotification`](avaudiosession/resumptionrecommendationnotification.md) Value is an [`AVAudioSession.ResumptionContext`](avaudiosession/resumptioncontext.md) describing the resumption recommendation.
- [AVAudioSession.DidBecomeActiveMessage](avaudiosession/didbecomeactivemessage.md)
- [AVAudioSession.DidBecomeInactiveMessage](avaudiosession/didbecomeinactivemessage.md)
- [AVAudioSession.ResumptionRecommendationMessage](avaudiosession/resumptionrecommendationmessage.md)
- [AVAudioSession.DeactivationResult](avaudiosession/deactivationresult.md)
  Type-safe representation of audio session deactivation results.
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