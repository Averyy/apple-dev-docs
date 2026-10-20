# uuid

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * UUID;
```

## See Also

### Accessing Call Attributes
- [var isOutgoing: Bool](./isoutgoing.md)
  A Boolean value that indicates whether the call is outgoing.
- [var hasConnected: Bool](./hasconnected.md)
  A Boolean value that indicates whether the call has connected.
- [var hasEnded: Bool](./hasended.md)
  A Boolean value that indicates whether the call has ended.
- [var isOnHold: Bool](./isonhold.md)
  A Boolean value that indicates whether the call is on hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcall/uuid)*