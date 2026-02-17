# messageHandler(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Handles incoming messages from the accessory.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
func messageHandler(_ message: AccessoryMessage)
```

## Parameters

- `message`: An accessory message that contains one or more payloads.

## See Also

- [func sendMessage(AccessoryMessage) async throws](accessoryfeaturesession/sendmessage(_:).md)
  Sends a message to the accessory through the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession/messagehandler(_:))*