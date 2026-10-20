# didInvalidate()

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Handles notification session termination.

**Availability**:
- iOS 26.5+

## Declaration

```swift
func didInvalidate()
```

#### Discussion

Clean up resources and clear stored session references when the system calls this method.

## See Also

- [func didActivate(for: NotificationsForwarding.Session)](notificationsforwarding/accessorynotificationshandler/didactivate(for:).md)
  Establishes a notification session for communication with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/didinvalidate())*