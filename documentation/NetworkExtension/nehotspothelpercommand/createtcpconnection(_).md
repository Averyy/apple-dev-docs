# createTCPConnection(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Create a new TCP connection over the network associated with the command.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Pass the Swift [`interface`](./interface-46dq.md) property or the ObjectiveC [`interface`](./interface-7rt15.md) property to the [`nw_parameters_require_interface(_:_:)`](../../Network/nw_parameters_require_interface%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func createTCPConnection(_ endpoint: NWEndpoint) -> NWTCPConnection
```

```objc
- (NWTCPConnection *) createTCPConnection:(NWEndpoint *) endpoint;
```

#### Return Value

A TCP connection that will connect over the network associated with the command.

#### Discussion

The TCP connection is started automatically. Use KVO to observe the connection’s `state` property to be notified when the connection is established or fails.

## Parameters

- `endpoint`: The remote host and port of the connection.

## See Also

### Networking on the hotspot network
- [func bind(to: NEHotspotHelperCommand)](../../Foundation/nsmutableurlrequest/bind%28to%29.md)
  Binds a URL request to the network interface associated with the hotspot helper command instance.
- [func createUDPSession(NWEndpoint) -> NWUDPSession](./createudpsession%28_%29.md)
  Creates a new UDP session over the network associated with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/createtcpconnection(_:))*