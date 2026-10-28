# hasConnected

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the call has connected.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var hasConnected: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL hasConnected;
```

## Discussion

A call is considered connected when both caller and callee can start communicating.

## See Also

### Accessing Call Attributes
- [var uuid: UUID](./uuid.md)
  The unique identifier for the call.
- [var isOutgoing: Bool](./isoutgoing.md)
  A Boolean value that indicates whether the call is outgoing.
- [var hasEnded: Bool](./hasended.md)
  A Boolean value that indicates whether the call has ended.
- [var isOnHold: Bool](./isonhold.md)
  A Boolean value that indicates whether the call is on hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcall/hasconnected)*