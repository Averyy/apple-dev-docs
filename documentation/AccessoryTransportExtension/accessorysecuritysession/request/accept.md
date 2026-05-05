# accept(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Accepts the session request with an event handler.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
final func accept<Handler>(_ sessionRequestHandler: () -> Handler) -> AccessorySecuritySession.Request.Decision where Handler : AccessorySecuritySession.EventHandler
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

The system invokes the handler with security events throughout the key exchange process.

## Parameters

- `sessionRequestHandler`: A closure that creates and returns an event handler.

## See Also

- [func reject(error: AccessorySecuritySession.Error?) -> AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/reject(error:).md)
  Rejects the session request with an optional error.
- [AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/decision.md)
  A structure that represents the decision to accept or reject a session request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/request/accept(_:))*