# resumptionContextKey

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

Keys for [`resumptionRecommendationNotification`](./resumptionrecommendationnotification.md) Value is an [`AVAudioSession.ResumptionContext`](./resumptioncontext.md) describing the resumption recommendation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
class let resumptionContextKey: String
```

```c
extern NSString * const AVAudioSessionResumptionContextKey;
```

## Mentions

- [Handling audio interruptions](../handling-audio-interruptions.md)

## See Also

### Observing activation lifecycle
- [class let didBecomeActiveNotification: NSNotification.Name](./didbecomeactivenotification.md)
  Notification sent when the audio session becomes active.
- [class let didBecomeInactiveNotification: NSNotification.Name](./didbecomeinactivenotification.md)
  Notification sent when the audio session becomes inactive.
- [class let resumptionRecommendationNotification: NSNotification.Name](./resumptionrecommendationnotification.md)
  Notification sent when the system provides a resumption recommendation.
- [class let deactivationContextKey: String](./deactivationcontextkey.md)
  Keys for [`didBecomeInactiveNotification`](./didbecomeinactivenotification.md) Value is an [`AVAudioSession.DeactivationContext`](./deactivationcontext.md) object describing the deactivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/resumptioncontextkey)*