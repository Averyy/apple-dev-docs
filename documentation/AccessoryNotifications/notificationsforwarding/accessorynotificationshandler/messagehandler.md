# messageHandler(_:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Handles decrypted messages received from the paired accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func messageHandler(_ message: TransportMessage)
```

#### Discussion

The system calls this method when your accessory sends data through the transport extension. The message arrives decrypted and ready for processing. Parse the message to determine the response type (notification action, user text input, or alert confirmation) and handle accordingly using the session’s response methods.

## Parameters

- `message`: The decrypted message payload from the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/messagehandler(_:))*