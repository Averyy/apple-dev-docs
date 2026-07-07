# sendSecurityMessage(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Sends a security message to the system.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func sendSecurityMessage(_ message: SecurityMessage) throws(AccessorySecuritySession.Error)
```

#### Discussion

Use this method to initiate key exchange by sending a [`SecurityMessage`](securitymessage.md) with [`SecurityMessage.KeyType.publicKey`](securitymessage/keytype-swift.enum/publickey.md). The system responds by calling your handler’s [`messageReceived(_:completion:)`](accessorysecuritysession/eventhandler/messagereceived(_:completion:).md) method with encapsulated key material.

## Parameters

- `message`: A security message containing key material.

## See Also

- [func cancel(error: AccessorySecuritySession.Error?)](accessorysecuritysession/cancel(error:).md)
  Cancels the security session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/sendsecuritymessage(_:))*