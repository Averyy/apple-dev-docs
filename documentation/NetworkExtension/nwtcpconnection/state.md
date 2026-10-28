# state

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The status of the connection.

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
var state: NWTCPConnectionState { get }
```

```objc
@property (nonatomic, readonly) NWTCPConnectionState state;
```

## Discussion

Use Key-Value Observing (KVO) to monitor the state. Many methods, such as reading and writing on the connection, are only valid when the state is `NWTCPConnectionStateConnected`. For information about KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Monitoring the connection status
- [enum NWTCPConnectionState](../nwtcpconnectionstate.md)
  Defined connection states. New types may be defined in the future.
- [var isViable: Bool](./isviable.md)
  The viability of a TCP connection indicates whether or not data can be transferred.
- [var error: (any Error)?](./error.md)
  The connection-wide error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/state)*