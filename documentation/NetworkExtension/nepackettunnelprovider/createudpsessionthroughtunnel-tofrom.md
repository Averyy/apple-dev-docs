# createUDPSessionThroughTunnel(to:from:)

**Framework**: Network Extension  
**Kind**: method

Creates a UDP session through the current tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func createUDPSessionThroughTunnel(to remoteEndpoint: NWEndpoint, from localEndpoint: NWHostEndpoint?) -> NWUDPSession
```

#### Discussion

Use this method to create a UDP session to an endpoint inside the private network.

## Parameters

- `remoteEndpoint`: The remote endpoint to send UDP datagrams to.
- `localEndpoint`: The local endpoint to bind the UDP session to. If nil, the UDP session will be bound to an ephemeral port on the virtual interface.

## See Also

- [func createTCPConnectionThroughTunnel(to: NWEndpoint, enableTLS: Bool, tlsParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection](nepackettunnelprovider/createtcpconnectionthroughtunnel(to:enabletls:tlsparameters:delegate:).md)
  Create a TCP connection through the current tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/createudpsessionthroughtunnel(to:from:))*