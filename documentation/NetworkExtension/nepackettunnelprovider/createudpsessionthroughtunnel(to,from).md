# createUDPSessionThroughTunnel(to:from:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Creates a UDP session through the current tunnel.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Pass the Swift [`virtualInterface`](./virtualinterface-7l3ol.md) property or the ObjectiveC [`virtualInterface`](./virtualinterface-9fpgd.md) property to the [`nw_parameters_require_interface(_:_:)`](../../Network/nw_parameters_require_interface%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func createUDPSessionThroughTunnel(to remoteEndpoint: NWEndpoint, from localEndpoint: NWHostEndpoint?) -> NWUDPSession
```

```objc
- (NWUDPSession *) createUDPSessionThroughTunnelToEndpoint:(NWEndpoint *) remoteEndpoint fromEndpoint:(NWHostEndpoint *) localEndpoint;
```

## Discussion

Use this method to create a UDP session to an endpoint inside the private network.

## Parameters

- `remoteEndpoint`: The remote endpoint to send UDP datagrams to.
- `localEndpoint`: The local endpoint to bind the UDP session to. If nil, the UDP session will be bound to an ephemeral port on the virtual interface.

## See Also

### Creating network connections through the tunnel
- [func createTCPConnectionThroughTunnel(to: NWEndpoint, enableTLS: Bool, tlsParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection](./createtcpconnectionthroughtunnel%28to,enabletls,tlsparameters,delegate%29.md)
  Create a TCP connection through the current tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/createudpsessionthroughtunnel(to:from:))*