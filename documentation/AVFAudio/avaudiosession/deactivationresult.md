# AVAudioSession.DeactivationResult

**Framework**: AVFAudio  
**Kind**: enum

Type-safe representation of audio session deactivation results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum DeactivationResult
```

#### Overview

This enum provides a Swift-idiomatic way to handle deactivation scenarios with associated values, ensuring impossible states are prevented at compile time.

## Topics

### Getting the deactivation result
- [AVAudioSession.DeactivationResult.appDeactivated](avaudiosession/deactivationresult/appdeactivated.md)
  Session was successfully deactivated by the app.
- [case systemInterruption(AVAudioSession.InterruptionContext)](avaudiosession/deactivationresult/systeminterruption(_:).md)
  Session was deactivated due to a system interruption.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [AVAudioSession.DeactivationContext](avaudiosession/deactivationcontext.md)
  An object that describes why and how the audio session deactivated.
- [AVAudioSession.DeactivationSource](avaudiosession/deactivationsource.md)
  The source of the audio session deactivation.
- [AVAudioSession.InterruptionContext](avaudiosession/interruptioncontext.md)
  An object that provides context about an audio session interruption.
- [AVAudioSession.ResumptionContext](avaudiosession/resumptioncontext.md)
  An object that provides context when resumption becomes available.
- [AVAudioSession.ResumptionRecommendation](avaudiosession/resumptionrecommendation.md)
  The system’s recommendation on whether to resume playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationresult)*