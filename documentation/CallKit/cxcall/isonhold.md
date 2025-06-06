# isOnHold

**Framework**: CallKit  
**Kind**: property

A Boolean value that indicates whether the call is on hold.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isOnHold: Bool { get }
```

#### Discussion

When a caller places the call on hold, callers are unable to communicate with one another until the holding caller removes the call from hold.

## See Also

- [var uuid: UUID](cxcall/uuid.md)
  The unique identifier for the call.
- [var isOutgoing: Bool](cxcall/isoutgoing.md)
  A Boolean value that indicates whether the call is outgoing.
- [var hasConnected: Bool](cxcall/hasconnected.md)
  A Boolean value that indicates whether the call has connected.
- [var hasEnded: Bool](cxcall/hasended.md)
  A Boolean value that indicates whether the call has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcall/isonhold)*