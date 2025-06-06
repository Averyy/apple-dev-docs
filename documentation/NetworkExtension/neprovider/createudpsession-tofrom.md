# createUDPSession(to:from:)

**Framework**: Network Extension  
**Kind**: method

Creates a UDP session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func createUDPSession(to remoteEndpoint: NWEndpoint, from localEndpoint: NWHostEndpoint?) -> NWUDPSession
```

#### Return Value

A [`NWUDPSession`](nwudpsession.md) object. The remote endpoint is in the process of being resolved. You can observe the session’s `state` property using KVO to determine when the session can be used to send and receive UDP datagrams.

#### Discussion

This method provides a convenient way to create UDP connections from a Network Extension Provider. It is preferred over using the sockets API. For instance, the Tunnel Provider can use this method to create a UDP connection with the tunnel server that can be used to tunnel network data.

## Parameters

- `remoteEndpoint`: The remote endpoint to send UDP datagrams to.
- `localEndpoint`: The local endpoint to bind the UDP session to. If nil, the UDP session will be bound to an ephemeral port on the primary physical interface.

## See Also

- [func createTCPConnection(to: NWEndpoint, enableTLS: Bool, tlsParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection](neprovider/createtcpconnection(to:enabletls:tlsparameters:delegate:).md)
  Create a TCP connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/createudpsession(to:from:))*