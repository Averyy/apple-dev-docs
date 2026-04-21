# removeNotifications(identifiers:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Removes the identified notifications.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func removeNotifications(identifiers: [AccessoryNotification.Identifier]) async throws
```

#### Discussion

This method has equivalent behavior to clearing notifications from Notification Center on the phone. The system doesn’t send actions to apps for removed notifications. This method only throws for errors receiving the removal request, not if some identifiers were already removed.

## Parameters

- `identifiers`: An array of notification identifiers to clear.

## See Also

- [func removeNotifications(withIdentifiers: [String], sourceIdentifier: String) async throws](notificationsforwarding/accessorynotificationssession/removenotifications(withidentifiers:sourceidentifier:).md)
  Removes notifications using primitive identifier components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession/removenotifications(identifiers:))*