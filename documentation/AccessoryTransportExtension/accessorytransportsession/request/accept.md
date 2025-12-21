# accept(_:)

**Framework**: AccessoryTransportExtension  
**Kind**: method

Accepts the session request and provides an event handler.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
final func accept<Handler>(_ sessionRequestHandler: () -> Handler) -> AccessoryTransportSession.Request.Decision where Handler : AccessoryTransportSession.EventHandler
```

## Parameters

- `sessionRequestHandler`: A closure that produces an   to handle session events.

## See Also

- [func reject(error: AccessoryTransportSession.Error?) -> AccessoryTransportSession.Request.Decision](accessorytransportsession/request/reject(error:).md)
  Rejects the session request.
- [AccessoryTransportSession.Request.Decision](accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/request/accept(_:))*