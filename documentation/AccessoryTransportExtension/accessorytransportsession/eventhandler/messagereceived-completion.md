# messageReceived(_:completion:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Message received from the Data Provider. Completion should be called with the result of sending the message to the accessory.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func messageReceived(_ message: TransportMessage, completion: @escaping @Sendable (AccessoryMessage.Result) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/messagereceived(_:completion:))*