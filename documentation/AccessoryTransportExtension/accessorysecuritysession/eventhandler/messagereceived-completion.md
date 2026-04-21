# messageReceived(_:completion:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Handles incoming key material from the system during key exchange.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
func messageReceived(_ message: SecurityMessage, completion: @escaping @Sendable (AccessoryMessage.Result) -> Void)
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

The system calls this method with a [`SecurityMessage`](securitymessage.md) containing [`SecurityMessage.KeyType.encapsulatedKey`](securitymessage/keytype-swift.enum/encapsulatedkey.md) after receiving your accessory’s public key. Forward the key material to your accessory via Bluetooth. Call the completion handler with [`AccessoryMessage.Result.success`](accessorymessage/result/success.md) if transmission succeeds, or [`AccessoryMessage.Result.failure(_:)`](accessorymessage/result/failure(_:).md) if an error occurs.

## Parameters

- `message`: A security message containing cryptographic key material.
- `completion`: A closure to call when message processing completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/eventhandler/messagereceived(_:completion:))*