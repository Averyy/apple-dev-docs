# send(message:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Send a message to the paired accessory.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func send(message: AccessoryMessage) async throws
```

#### Discussion

> **Note**: An error if the message could not be sent.

## Parameters

- `message`: The message to send to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession/send(message:))*