# sendMessage(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Sends a message to the accessory through the system.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
func sendMessage(_ accessoryMessage: AccessoryMessage) async throws
```

#### Discussion

The system encrypts the message before delivering it to your app’s transport extension for transmission to the accessory.

## Parameters

- `accessoryMessage`: An accessory message to send to the accessory.

## See Also

- [func messageHandler(AccessoryMessage)](accessoryfeaturesession/messagehandler(_:).md)
  Handles incoming messages from the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession/sendmessage(_:))*