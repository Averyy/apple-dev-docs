# textMessageAvailabilityDidChange

**Framework**: Foundation  
**Kind**: property

Notification posted when text message availability changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var textMessageAvailabilityDidChange: NotificationCenter.BaseMessageIdentifier<MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage> { get }
```

#### Discussion

This notification is posted when the device’s ability to send text messages changes (e.g., SIM card inserted/removed, airplane mode toggled, iMessage account status changed).

> **Note**: This notification may be delivered on any thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/textmessageavailabilitydidchange)*