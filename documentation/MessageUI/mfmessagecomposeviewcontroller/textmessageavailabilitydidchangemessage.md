# MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage

**Framework**: Message UI  
**Kind**: struct  
**Role**: Structure

Message type for text message availability change notifications.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TextMessageAvailabilityDidChangeMessage
```

#### Overview

This notification is posted when the value of `+canSendText` changes, indicating whether the device can send text messages.

> **Note**: This notification may be delivered on any thread. Observers should dispatch to the main actor if needed for UI updates.

## Topics

### Initializers
- [init(canSendText: Bool)](./textmessageavailabilitydidchangemessage/init%28cansendtext%29.md)
  Initialize with text message availability status
### Instance Properties
- [var canSendText: Bool](./textmessageavailabilitydidchangemessage/cansendtext.md)
  Whether text messages can be sent on this device
### Type Aliases
- [MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage.Subject](./textmessageavailabilitydidchangemessage/subject.md)
  The notification subject type
### Type Properties
- [static var name: Notification.Name](./textmessageavailabilitydidchangemessage/name.md)
  The existing Objective-C notification name
### Type Methods
- [static func makeMessage(Notification) -> MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage?](./textmessageavailabilitydidchangemessage/makemessage%28_%29.md)
  Transform a legacy Notification into a type-safe Message
- [static func makeNotification(MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage) -> Notification](./textmessageavailabilitydidchangemessage/makenotification%28_%29.md)
  Transform a type-safe Message into a legacy Notification

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage)*