# activate(for:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Establishes a notification session for communication between the extension and the system.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func activate(for session: NotificationsForwarding.Session)
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

Store the session reference to use across multiple notification life cycle events.

## Parameters

- `session`: A session object that enables communication with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/activate(for:))*