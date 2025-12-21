# reject(error:)

**Framework**: AccessoryTransportExtension  
**Kind**: method

Rejects the session request.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
final func reject(error: AccessoryTransportSession.Error?) -> AccessoryTransportSession.Request.Decision
```

## Parameters

- `error`: An error that indicates why the extension rejected the request.

## See Also

- [func accept<Handler>(() -> Handler) -> AccessoryTransportSession.Request.Decision](accessorytransportsession/request/accept(_:).md)
  Accepts the session request and provides an event handler.
- [AccessoryTransportSession.Request.Decision](accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/request/reject(error:))*