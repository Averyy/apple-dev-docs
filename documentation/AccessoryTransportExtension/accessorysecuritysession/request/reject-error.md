# reject(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Rejects the session request with an optional error.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
final func reject(error: AccessorySecuritySession.Error?) -> AccessorySecuritySession.Request.Decision
```

## Parameters

- `error`: An optional error that indicates the reason for rejection.

## See Also

- [func accept<Handler>(() -> Handler) -> AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/accept(_:).md)
  Accepts the session request with an event handler.
- [AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/decision.md)
  A structure that represents the decision to accept or reject a session request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/request/reject(error:))*