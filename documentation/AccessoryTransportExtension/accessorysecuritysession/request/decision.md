# AccessorySecuritySession.Request.Decision

**Framework**: Accessory Transport Extension  
**Kind**: struct  
**Role**: Structure

A structure that represents the decision to accept or reject a session request.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Decision
```

#### Overview

The [`accept(_:)`](./accept%28_%29.md) and [`reject(error:)`](./reject%28error%29.md) methods return this type.

## See Also

### Responding to the request
- [func accept<Handler>(() -> Handler) -> AccessorySecuritySession.Request.Decision](./accept%28_%29.md)
  Accepts the session request with an event handler.
- [func reject(error: AccessorySecuritySession.Error?) -> AccessorySecuritySession.Request.Decision](./reject%28error%29.md)
  Rejects the session request with an optional error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/request/decision)*