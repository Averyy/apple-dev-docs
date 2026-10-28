# didBecomeActiveNotification

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

Notification sent when the audio session becomes active.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
class let didBecomeActiveNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVAudioSessionDidBecomeActiveNotification;
```

## Mentions

- [Handling audio interruptions](../handling-audio-interruptions.md)

## Discussion

This notification has no userInfo payload.

## See Also

### Observing activation lifecycle
- [class let didBecomeInactiveNotification: NSNotification.Name](./didbecomeinactivenotification.md)
  Notification sent when the audio session becomes inactive.
- [class let resumptionRecommendationNotification: NSNotification.Name](./resumptionrecommendationnotification.md)
  Notification sent when the system provides a resumption recommendation.
- [class let deactivationContextKey: String](./deactivationcontextkey.md)
  Keys for [`didBecomeInactiveNotification`](./didbecomeinactivenotification.md) Value is an [`AVAudioSession.DeactivationContext`](./deactivationcontext.md) object describing the deactivation.
- [class let resumptionContextKey: String](./resumptioncontextkey.md)
  Keys for [`resumptionRecommendationNotification`](./resumptionrecommendationnotification.md) Value is an [`AVAudioSession.ResumptionContext`](./resumptioncontext.md) describing the resumption recommendation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/didbecomeactivenotification)*