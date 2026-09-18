# deactivationContextKey

**Framework**: AVFAudio  
**Kind**: property

Keys for [`didBecomeInactiveNotification`](avaudiosession/didbecomeinactivenotification.md) Value is an [`AVAudioSession.DeactivationContext`](avaudiosession/deactivationcontext.md) object describing the deactivation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
class let deactivationContextKey: String
```

## See Also

- [class let didBecomeActiveNotification: NSNotification.Name](avaudiosession/didbecomeactivenotification.md)
  Notification sent when the audio session becomes active.
- [class let didBecomeInactiveNotification: NSNotification.Name](avaudiosession/didbecomeinactivenotification.md)
  Notification sent when the audio session becomes inactive.
- [class let resumptionRecommendationNotification: NSNotification.Name](avaudiosession/resumptionrecommendationnotification.md)
  Notification sent when the system provides a resumption recommendation.
- [class let resumptionContextKey: String](avaudiosession/resumptioncontextkey.md)
  Keys for [`resumptionRecommendationNotification`](avaudiosession/resumptionrecommendationnotification.md) Value is an [`AVAudioSession.ResumptionContext`](avaudiosession/resumptioncontext.md) describing the resumption recommendation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationcontextkey)*