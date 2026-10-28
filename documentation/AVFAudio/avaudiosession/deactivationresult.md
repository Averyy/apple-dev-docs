# AVAudioSession.DeactivationResult

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

## Mentions

- [Handling audio interruptions](../handling-audio-interruptions.md)

## Overview

This enum provides a Swift-idiomatic way to handle deactivation scenarios with associated values, ensuring impossible states are prevented at compile time.

## Topics

### Getting the deactivation result
- [AVAudioSession.DeactivationResult.appDeactivated](./deactivationresult/appdeactivated.md)
  Session was successfully deactivated by the app.
- [case systemInterruption(AVAudioSession.InterruptionContext)](./deactivationresult/systeminterruption%28_%29.md)
  Session was deactivated due to a system interruption.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling activation messages
- [AVAudioSession.DidBecomeActiveMessage](./didbecomeactivemessage.md)
- [AVAudioSession.DidBecomeInactiveMessage](./didbecomeinactivemessage.md)
- [AVAudioSession.ResumptionRecommendationMessage](./resumptionrecommendationmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/deactivationresult)*