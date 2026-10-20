# init(socksv5Proxy:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a SOCKSv5 proxy configuration.

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
init(socksv5Proxy: NWEndpoint)
```

## Parameters

- `socksv5Proxy`: A host endpoint identifying the SOCKS proxy server.

## See Also

### Creating Proxy Configurations
- [init(relayHops: [ProxyConfiguration.RelayHop])](./init%28relayhops%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [ProxyConfiguration.RelayHop](./relayhop.md)
  A single relay server you can chain together with other servers.
- [init(httpCONNECTProxy: NWEndpoint, tlsOptions: NWProtocolTLS.Options?)](./init%28httpconnectproxy,tlsoptions%29.md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration/init(socksv5proxy:))*