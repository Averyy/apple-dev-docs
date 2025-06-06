# hasEnded

**Framework**: CallKit  
**Kind**: property

A Boolean value that indicates whether the call has ended.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var hasEnded: Bool { get }
```

#### Discussion

A call is considered ended when the user disconnects or all other callers disconnect.

## See Also

- [var uuid: UUID](cxcall/uuid.md)
  The unique identifier for the call.
- [var isOutgoing: Bool](cxcall/isoutgoing.md)
  A Boolean value that indicates whether the call is outgoing.
- [var hasConnected: Bool](cxcall/hasconnected.md)
  A Boolean value that indicates whether the call has connected.
- [var isOnHold: Bool](cxcall/isonhold.md)
  A Boolean value that indicates whether the call is on hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcall/hasended)*