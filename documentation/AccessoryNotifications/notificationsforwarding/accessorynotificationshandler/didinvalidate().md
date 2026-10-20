# didInvalidate()

**Framework**: Accessory Notifications  
**Kind**: method  
**Role**: Instance Method  
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

### Managing the session life cycle
- [func didActivate(for: NotificationsForwarding.Session)](./didactivate%28for%29.md)
  Establishes a notification session for communication with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/didinvalidate())*