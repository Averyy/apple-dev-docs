# NotificationResponse

**Framework**: Accessory Notifications  
**Kind**: struct  
**Role**: Structure

A structure that represents a person’s response to a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct NotificationResponse
```

## Mentions

- [Responding to forwarded notifications](./responding-to-forwarded-notifications.md)

## Overview

Create an instance of this structure when a person responds to a notification on your accessory. Send it to the system using [`sendResponse(_:)`](./notificationsforwarding/accessorynotificationssession/sendresponse%28_%29.md) after receiving the response data through [`messageHandler(_:)`](./notificationsforwarding/accessorynotificationshandler/messagehandler%28_%29.md).

## Topics

### Creating a notification response
- [init(sourceIdentifier: String, notificationIdentifier: String, actionIdentifier: String, userText: String?)](./notificationresponse/init%28sourceidentifier,notificationidentifier,actionidentifier,usertext%29.md)
  Initializes a notification response with the given identifiers and optional user text.
### Identifying the response action
- [var actionIdentifier: String](./notificationresponse/actionidentifier.md)
  An identifier for the action the person took with the notification.
### Identifying the notification
- [var notificationIdentifier: String](./notificationresponse/notificationidentifier.md)
  An identifier for the notification.
- [var sourceIdentifier: String](./notificationresponse/sourceidentifier.md)
  A bundle identifier for the app that sent the notification.
### Accessing user-provided text
- [var userText: String?](./notificationresponse/usertext.md)
  A text string that a person provides in response to the notification.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)

## See Also

### Interactive support
- [Responding to forwarded notifications](./responding-to-forwarded-notifications.md)
  Enable people to interact with notifications on your accessory and convey their responses to iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationresponse)*