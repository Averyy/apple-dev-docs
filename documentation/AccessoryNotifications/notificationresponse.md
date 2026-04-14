# NotificationResponse

**Framework**: Accessory Notifications  
**Kind**: struct

A person’s response to a notification.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
struct NotificationResponse
```

#### Overview

Create an instance of this structure when a person responds to a notification on your accessory, and send it back to your app.

> ❗ **Important**: The Accessory Notifications framework will support this feature in a future release.

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