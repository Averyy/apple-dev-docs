# NotificationResponse

**Framework**: Accessory Notifications  
**Kind**: struct

A structure that represents a person’s response to a notification.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct NotificationResponse
```

#### Overview

Create an instance of this structure when a person responds to a notification on your accessory. Send it to the system using [`sendResponse(_:)`](notificationsforwarding/accessorynotificationssession/sendresponse(_:).md) after receiving the response data through [`messageHandler(_:)`](notificationsforwarding/accessorynotificationshandler/messagehandler(_:).md).

> **Note**: Notification responses currently support Bluetooth transport only. The accessory sends encrypted response data to the transport extension, which forwards it to the data provider for processing.

## Topics

### Creating a notification response
- [init(sourceIdentifier: String, notificationIdentifier: String, actionIdentifier: String, userText: String?)](notificationresponse/init(sourceidentifier:notificationidentifier:actionidentifier:usertext:).md)
  Initializes a notification response with the given identifiers and optional user text.
### Identifying the response action
- [var actionIdentifier: String](notificationresponse/actionidentifier.md)
  An identifier for the action the person took with the notification.
### Identifying the notification
- [var notificationIdentifier: String](notificationresponse/notificationidentifier.md)
  An identifier for the notification.
- [var sourceIdentifier: String](notificationresponse/sourceidentifier.md)
  A bundle identifier for the app that sent the notification.
### Accessing user-provided text
- [var userText: String?](notificationresponse/usertext.md)
  A text string that a person provides in response to the notification.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationresponse)*