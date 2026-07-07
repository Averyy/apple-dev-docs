# AccessorySecuritySession.Request.Decision

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that represents the decision to accept or reject a session request.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct Decision
```

#### Overview

The [`accept(_:)`](accessorysecuritysession/request/accept(_:).md) and [`reject(error:)`](accessorysecuritysession/request/reject(error:).md) methods return this type.

## See Also

- [func accept<Handler>(() -> Handler) -> AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/accept(_:).md)
  Accepts the session request with an event handler.
- [func reject(error: AccessorySecuritySession.Error?) -> AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/reject(error:).md)
  Rejects the session request with an optional error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/request/decision)*