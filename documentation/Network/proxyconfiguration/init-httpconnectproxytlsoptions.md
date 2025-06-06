# init(httpCONNECTProxy:tlsOptions:)

**Framework**: Network  
**Kind**: init

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

These HTTP CONNECT proxies only handle TCP connections. To support UDP proxying, use [`init(relayHops:)`](proxyconfiguration/init(relayhops:).md).

## Parameters

- `httpCONNECTProxy`: A host endpoint identifying the proxy server accessible using HTTP/1.1.
- `tlsOptions`: Optional TLS options to use for a TLS handshake to the relay. If no TLS options are provided, the proxy will be accessed using cleartext HTTP.

## See Also

- [init(relayHops: [ProxyConfiguration.RelayHop])](proxyconfiguration/init(relayhops:).md)
  Initializes a proxy configuration with one or two relay hops.
- [ProxyConfiguration.RelayHop](proxyconfiguration/relayhop.md)
  A single relay server you can chain together with other servers.
- [init(socksv5Proxy: NWEndpoint)](proxyconfiguration/init(socksv5proxy:).md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration/init(httpconnectproxy:tlsoptions:))*