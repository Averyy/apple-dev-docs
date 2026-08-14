# MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage

**Framework**: Message UI  
**Kind**: struct

Message type for text message availability change notifications.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TextMessageAvailabilityDidChangeMessage
```

#### Overview

This notification is posted when the value of `+canSendText` changes, indicating whether the device can send text messages.

> **Note**: This notification may be delivered on any thread. Observers should dispatch to the main actor if needed for UI updates.

## Topics

### Initializers
- [init(canSendText: Bool)](mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/init(cansendtext:).md)
  Initialize with text message availability status
### Instance Properties
- [var canSendText: Bool](mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/cansendtext.md)
  Whether text messages can be sent on this device
### Type Aliases
- [MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage.Subject](mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/subject.md)
  The notification subject type
### Type Properties
- [static var name: Notification.Name](mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/name.md)
  The existing Objective-C notification name
### Type Methods
- [static func makeMessage(Notification) -> MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage?](mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/makemessage(_:).md)
  Transform a legacy Notification into a type-safe Message
- [static func makeNotification(MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage) -> Notification](mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/makenotification(_:).md)
  Transform a type-safe Message into a legacy Notification

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../foundation/notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage)*