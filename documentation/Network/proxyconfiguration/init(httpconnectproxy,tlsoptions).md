# init(httpCONNECTProxy:tlsOptions:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(httpCONNECTProxy: NWEndpoint, tlsOptions: NWProtocolTLS.Options? = nil)
```

#### Discussion

These HTTP CONNECT proxies only handle TCP connections. To support UDP proxying, use [`init(relayHops:)`](./init%28relayhops%29.md).

## Parameters

- `httpCONNECTProxy`: A host endpoint identifying the proxy server accessible using HTTP/1.1.
- `tlsOptions`: Optional TLS options to use for a TLS handshake to the relay. If no TLS options are provided, the proxy will be accessed using cleartext HTTP.

## See Also

### Creating Proxy Configurations
- [init(relayHops: [ProxyConfiguration.RelayHop])](./init%28relayhops%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [ProxyConfiguration.RelayHop](./relayhop.md)
  A single relay server you can chain together with other servers.
- [init(socksv5Proxy: NWEndpoint)](./init%28socksv5proxy%29.md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration/init(httpconnectproxy:tlsoptions:))*