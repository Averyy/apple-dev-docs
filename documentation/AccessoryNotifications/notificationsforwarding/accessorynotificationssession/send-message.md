# send(message:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Sends a message to the paired accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func send(message: AccessoryMessage) async throws
```

#### Discussion

Create an [`AccessoryMessage`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryMessage) containing your notification data and send it to your accessory. The system encrypts the message before delivering it to the transport extension for transmission.

## Parameters

- `message`: The message to send to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession/send(message:))*