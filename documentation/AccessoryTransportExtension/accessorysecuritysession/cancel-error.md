# cancel(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Cancels the security session.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func cancel(error: AccessorySecuritySession.Error?)
```

## Parameters

- `error`: An optional error that indicates the reason for cancellation.

## See Also

- [func sendSecurityMessage(SecurityMessage) throws(AccessorySecuritySession.Error)](accessorysecuritysession/sendsecuritymessage(_:).md)
  Sends a security message to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/cancel(error:))*