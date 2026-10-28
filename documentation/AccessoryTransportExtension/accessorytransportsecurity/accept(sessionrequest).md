# accept(sessionRequest:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Evaluates incoming security session requests for an accessory.

**Availability**:
- iOS 26.5+

## Declaration

```swift
func accept(sessionRequest: AccessorySecuritySession.Request) -> AccessorySecuritySession.Request.Decision
```

## Discussion

Return a decision by calling either [`accept(_:)`](../accessorysecuritysession/request/accept%28_%29.md) or [`reject(error:)`](../accessorysecuritysession/request/reject%28error%29.md) on the request.

## Parameters

- `sessionRequest`: A request object that represents the incoming session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity/accept(sessionrequest:))*