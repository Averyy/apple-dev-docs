# sendSecurityEvent(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Sends a security event to the system.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
func sendSecurityEvent(_ event: AccessorySecurity.Event) throws
```

#### Discussion

Use this method to send key exchange events such as [`AccessorySecurity.Event.keyReply(ciphersuite:publicKey:)`](accessorysecurity/event/keyreply(ciphersuite:publickey:).md) and [`AccessorySecurity.Event.encapsulatedKey(_:)`](accessorysecurity/event/encapsulatedkey(_:).md).

## Parameters

- `event`: A security event to send.

## See Also

- [func cancel(error: (any Error)?)](accessorysecuritysession/cancel(error:).md)
  Cancels the security session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/sendsecurityevent(_:))*