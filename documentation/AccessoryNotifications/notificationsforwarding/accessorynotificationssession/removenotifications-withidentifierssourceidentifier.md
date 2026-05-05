# removeNotifications(withIdentifiers:sourceIdentifier:)

**Framework**: Accessory Notifications  
**Kind**: method

Removes notifications using primitive identifier components.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func removeNotifications(withIdentifiers identifiers: [String], sourceIdentifier: String) async throws
```

#### Discussion

This method provides an alternative way to remove notifications using string identifiers rather than [`AccessoryNotification.Identifier`](accessorynotification/identifier-swift.struct.md) instances.

## Parameters

- `identifiers`: A set of notification identifier strings.
- `sourceIdentifier`: The bundle identifier of the app that posted the notifications.

## See Also

- [func removeNotifications(identifiers: [AccessoryNotification.Identifier]) async throws](notificationsforwarding/accessorynotificationssession/removenotifications(identifiers:).md)
  Removes the identified notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession/removenotifications(withidentifiers:sourceidentifier:))*