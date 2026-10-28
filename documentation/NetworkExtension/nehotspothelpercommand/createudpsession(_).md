# createUDPSession(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Creates a new UDP session over the network associated with the command.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Pass the Swift [`interface`](./interface-46dq.md) property or the ObjectiveC [`interface`](./interface-7rt15.md) property to the [`nw_parameters_require_interface(_:_:)`](../../Network/nw_parameters_require_interface%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func createUDPSession(_ endpoint: NWEndpoint) -> NWUDPSession
```

```objc
- (NWUDPSession *) createUDPSession:(NWEndpoint *) endpoint;
```

## Return Value

A UDP session that will connect over the network associated with the command.

## Discussion

The UDP session is started automatically. Use KVO to observe the session’s state property to be notified when the session is ready to send and receive UDP datagrams. For information about KVO see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Parameters

- `endpoint`: The remote host and port of the session.

## See Also

### Networking on the hotspot network
- [func bind(to: NEHotspotHelperCommand)](../../Foundation/nsmutableurlrequest/bind%28to%29.md)
  Binds a URL request to the network interface associated with the hotspot helper command instance.
- [func createTCPConnection(NWEndpoint) -> NWTCPConnection](./createtcpconnection%28_%29.md)
  Create a new TCP connection over the network associated with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/createudpsession(_:))*