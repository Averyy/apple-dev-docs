# accept(sessionRequest:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Evaluates incoming security session requests for an accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
func accept(sessionRequest: AccessorySecuritySession.Request) -> AccessorySecuritySession.Request.Decision
```

#### Discussion

Return a decision by calling either [`accept(_:)`](accessorysecuritysession/request/accept(_:).md) or [`reject(error:)`](accessorysecuritysession/request/reject(error:).md) on the request.

## Parameters

- `sessionRequest`: A request object that represents the incoming session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity/accept(sessionrequest:))*