# createTCPConnection(to:enableTLS:tlsParameters:delegate:)

**Framework**: Network Extension  
**Kind**: method

Create a TCP connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func createTCPConnection(to remoteEndpoint: NWEndpoint, enableTLS: Bool, tlsParameters TLSParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection
```

#### Return Value

A [`NWTCPConnection`](nwtcpconnection.md) object. The underlying connection is in the process of being established. You can observe the connection’s `state` property using KVO to determine when the connection is successfully established or fails due to an error. For information about KVO, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

#### Discussion

This method provides a convenient way to create TCP connections from a Network Extension Provider. It is preferred over using the sockets API. For instance, the Tunnel Provider can use this method to create a secure TCP connection with the tunnel server that can be used to tunnel network data.

## Parameters

- `remoteEndpoint`: The remote endpoint to connect to.
- `enableTLS`: A flag indicating if the TLS protocol should be used to secure the communication over the connection.
- `TLSParameters`: The TLS protocol parameters to use. If   is   and this parameter is nil then the default TLS parameters will be used.
- `delegate`: An optional delegate object that conforms to the   protocol.

## See Also

- [func createUDPSession(to: NWEndpoint, from: NWHostEndpoint?) -> NWUDPSession](neprovider/createudpsession(to:from:).md)
  Creates a UDP session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/createtcpconnection(to:enabletls:tlsparameters:delegate:))*