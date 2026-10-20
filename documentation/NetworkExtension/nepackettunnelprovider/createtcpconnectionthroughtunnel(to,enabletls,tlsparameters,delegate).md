# createTCPConnectionThroughTunnel(to:enableTLS:tlsParameters:delegate:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Create a TCP connection through the current tunnel.

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
func createTCPConnectionThroughTunnel(to remoteEndpoint: NWEndpoint, enableTLS: Bool, tlsParameters TLSParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection
```

```objc
- (NWTCPConnection *) createTCPConnectionThroughTunnelToEndpoint:(NWEndpoint *) remoteEndpoint enableTLS:(BOOL) enableTLS TLSParameters:(NWTLSParameters *) TLSParameters delegate:(id) delegate;
```

#### Discussion

Use this method to create a TCP connection to an endpoint inside the private network.

## Parameters

- `remoteEndpoint`: The remote endpoint to connect to.
- `enableTLS`: A flag indicating if the TLS protocol should be used to secure the communication over the connection.
- `TLSParameters`: The TLS protocol parameters to use. If `enableTLS` is [`true`](../../Swift/true.md) and this parameter is nil then the default TLS parameters will be used.
- `delegate`: An optional delegate object that conforms to the [`NWTCPConnectionAuthenticationDelegate`](../nwtcpconnectionauthenticationdelegate.md) protocol.

## See Also

### Creating network connections through the tunnel
- [func createUDPSessionThroughTunnel(to: NWEndpoint, from: NWHostEndpoint?) -> NWUDPSession](./createudpsessionthroughtunnel%28to,from%29.md)
  Creates a UDP session through the current tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/createtcpconnectionthroughtunnel(to:enabletls:tlsparameters:delegate:))*