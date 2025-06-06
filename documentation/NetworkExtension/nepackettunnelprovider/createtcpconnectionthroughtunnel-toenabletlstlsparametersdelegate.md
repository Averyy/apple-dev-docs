# createTCPConnectionThroughTunnel(to:enableTLS:tlsParameters:delegate:)

**Framework**: Network Extension  
**Kind**: method

Create a TCP connection through the current tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func createTCPConnectionThroughTunnel(to remoteEndpoint: NWEndpoint, enableTLS: Bool, tlsParameters TLSParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection
```

#### Discussion

Use this method to create a TCP connection to an endpoint inside the private network.

## Parameters

- `remoteEndpoint`: The remote endpoint to connect to.
- `enableTLS`: A flag indicating if the TLS protocol should be used to secure the communication over the connection.
- `TLSParameters`: The TLS protocol parameters to use. If   is   and this parameter is nil then the default TLS parameters will be used.
- `delegate`: An optional delegate object that conforms to the   protocol.

## See Also

- [func createUDPSessionThroughTunnel(to: NWEndpoint, from: NWHostEndpoint?) -> NWUDPSession](nepackettunnelprovider/createudpsessionthroughtunnel(to:from:).md)
  Creates a UDP session through the current tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/createtcpconnectionthroughtunnel(to:enabletls:tlsparameters:delegate:))*