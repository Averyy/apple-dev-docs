# didActivate(for:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Establishes a notification session for communication with the system.

**Availability**:
- iOS 26.5+

## Declaration

```swift
func didActivate(for session: NotificationsForwarding.Session)
```

#### Discussion

Store the session reference to use across multiple notification life cycle events for sending messages to your accessory and communicating responses back to the system.

## Parameters

- `session`: A session object that enables communication with the system.

## See Also

### Managing the session life cycle
- [func didInvalidate()](./didinvalidate%28%29.md)
  Handles notification session termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/didactivate(for:))*