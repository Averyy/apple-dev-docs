# updateNotification(_:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Updates a notification with new content.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func updateNotification(_ notification: AccessoryNotification)
```

#### Discussion

Accessories don’t need to alert the person for notification updates; update the displayed notification content without triggering additional alerts.

## Parameters

- `notification`: The notification with updated details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/updatenotification(_:))*