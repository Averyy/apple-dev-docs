# isViable

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The viability of a TCP connection indicates whether or not data can be transferred.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_set_viability_changed_handler(_:_:)`](../../Network/nw_connection_set_viability_changed_handler%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var isViable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isViable) BOOL viable;
```

#### Discussion

Evaluates to [`true`](../../Swift/true.md) if the connection can read and write data, [`false`](../../Swift/false.md) otherwise. Use Key-Value Observing to watch this property.

## See Also

### Monitoring the connection status
- [var state: NWTCPConnectionState](./state.md)
  The status of the connection.
- [enum NWTCPConnectionState](../nwtcpconnectionstate.md)
  Defined connection states. New types may be defined in the future.
- [var error: (any Error)?](./error.md)
  The connection-wide error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/isviable)*