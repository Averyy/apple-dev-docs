# init(sourceIdentifier:notificationIdentifier:actionIdentifier:userText:)

**Framework**: Accessory Notifications  
**Kind**: init

Initializes a notification response with the given identifiers and optional user text.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
init(sourceIdentifier: String, notificationIdentifier: String, actionIdentifier: String, userText: String?)
```

## Parameters

- `sourceIdentifier`: The bundle identifier of the app that sent the notification.
- `notificationIdentifier`: The identifier for the notification.
- `actionIdentifier`: The identifier for the action taken.
- `userText`: Optional text provided by the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationresponse/init(sourceidentifier:notificationidentifier:actionidentifier:usertext:))*