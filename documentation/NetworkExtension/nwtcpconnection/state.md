# state

**Framework**: Network Extension  
**Kind**: property

The status of the connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var state: NWTCPConnectionState { get }
```

#### Discussion

Use Key-Value Observing (KVO) to monitor the state. Many methods, such as reading and writing on the connection, are only valid when the state is `NWTCPConnectionStateConnected`. For information about KVO, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [enum NWTCPConnectionState](nwtcpconnectionstate.md)
  Defined connection states. New types may be defined in the future.
- [var isViable: Bool](nwtcpconnection/isviable.md)
  The viability of a TCP connection indicates whether or not data can be transferred.
- [var error: (any Error)?](nwtcpconnection/error.md)
  The connection-wide error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/state)*