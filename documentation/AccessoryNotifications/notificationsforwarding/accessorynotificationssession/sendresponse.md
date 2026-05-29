# sendResponse(_:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Sends a notification response from the accessory to the system.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func sendResponse(_ response: NotificationResponse) async throws
```

#### Discussion

After receiving a message through [`messageHandler(_:)`](notificationsforwarding/accessorynotificationshandler/messagehandler(_:).md), parse the accessory’s response data and create a [`NotificationResponse`](notificationresponse.md) instance. Call this method to deliver the response to the system for handling.

> **Note**: The response data arrives decrypted in `messageHandler(_:)`. Your extension needs to parse the data according to the format your accessory uses and then extract the notification identifiers and action details.

## Parameters

- `response`: The notification response from the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession/sendresponse(_:))*