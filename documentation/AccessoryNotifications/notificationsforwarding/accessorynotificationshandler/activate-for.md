# activate(for:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Establishes a notification session for communication between the extension and the system.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
func activate(for session: NotificationsForwarding.Session)
```

#### Discussion

Store the session reference to use across multiple notification life cycle events.

## Parameters

- `session`: A session object that enables communication with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/activate(for:))*