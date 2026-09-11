# AVAudioUnitComponentManager.RegistrationsChangedMessage

**Framework**: AVFAudio  
**Kind**: struct

Type-safe notification message for audio unit component registration changes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct RegistrationsChangedMessage
```

#### Overview

This notification is posted when the system’s audio component registrations have changed, such as when audio units are installed or removed. The notification object is the shared `AVAudioUnitComponentManager` instance.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../foundation/notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class let registrationsChangedNotification: NSNotification.Name](avaudiounitcomponentmanager/registrationschangednotification.md)
  A notification the component manager generates when it updates its list of components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/registrationschangedmessage)*