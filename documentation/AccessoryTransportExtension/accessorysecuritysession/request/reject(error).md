# reject(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Rejects the session request with an optional error.

**Availability**:
- iOS 26.5+

## Declaration

```swift
final func reject(error: AccessorySecuritySession.Error?) -> AccessorySecuritySession.Request.Decision
```

## Parameters

- `error`: An optional error that indicates the reason for rejection.

## See Also

### Responding to the request
- [func accept<Handler>(() -> Handler) -> AccessorySecuritySession.Request.Decision](./accept%28_%29.md)
  Accepts the session request with an event handler.
- [AccessorySecuritySession.Request.Decision](./decision.md)
  A structure that represents the decision to accept or reject a session request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/request/reject(error:))*