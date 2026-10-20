# state

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The current state of the UDP session.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_set_state_changed_handler(_:_:)`](../../Network/nw_connection_set_state_changed_handler%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var state: NWUDPSessionState { get }
```

```objc
@property (nonatomic, readonly) NWUDPSessionState state;
```

#### Discussion

Use Key-Value Observing (KVO) to monitor the state. If the state is `NWUDPSessionStateReady`, then the connection is eligible for reading and writing. The state will be `NWUDPSessionStateFailed` if the endpoint could not be resolved, or all endpoints have been rejected. For information about KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Monitoring the session state
- [enum NWUDPSessionState](../nwudpsessionstate.md)
- [var isViable: Bool](./isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/state)*