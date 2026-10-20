# cancel(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Cancels the security session.

**Availability**:
- iOS 26.5+

## Declaration

```swift
func cancel(error: AccessorySecuritySession.Error?)
```

## Parameters

- `error`: An optional error that indicates the reason for cancellation.

## See Also

### Managing the session life cycle
- [func sendSecurityMessage(SecurityMessage) throws(AccessorySecuritySession.Error)](./sendsecuritymessage%28_%29.md)
  Sends a security message to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/cancel(error:))*