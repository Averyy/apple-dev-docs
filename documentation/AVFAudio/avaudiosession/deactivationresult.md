# AVAudioSession.DeactivationResult

**Framework**: AVFAudio  
**Kind**: enum

Type-safe representation of audio session deactivation results.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [AVAudioSession.DidBecomeActiveMessage](avaudiosession/didbecomeactivemessage.md)
- [AVAudioSession.DidBecomeInactiveMessage](avaudiosession/didbecomeinactivemessage.md)
- [AVAudioSession.ResumptionRecommendationMessage](avaudiosession/resumptionrecommendationmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationresult)*