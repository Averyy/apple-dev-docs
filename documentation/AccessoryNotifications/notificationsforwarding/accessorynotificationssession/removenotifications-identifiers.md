# removeNotifications(identifiers:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Remove notifications.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func removeNotifications(identifiers: [AccessoryNotification.Identifier]) async throws
```

#### Discussion

- identifiers: An array of notification identifiers to clear.

> **Note**: An error if the system could not receive the request to remove notifications.

This method has equivalent behavior to clearing the same notifications from Notification Center on the phone. Actions are not sent to the app for removed notifications. This method only throws for errors receiving the request to remove notifications. It does not throw if some of the identifiers could not be cleared because they have already been removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession/removenotifications(identifiers:))*