# sendResponse(_:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Send a notification response from an accessory.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func sendResponse(_ response: NotificationResponse) async throws
```

#### Discussion

> **Note**: An error if the response could not be accepted by the system.

## Parameters

- `response`: The notification response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession/sendresponse(_:))*