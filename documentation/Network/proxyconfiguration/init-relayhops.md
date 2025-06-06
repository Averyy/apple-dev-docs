# init(relayHops:)

**Framework**: Network  
**Kind**: init

Initializes a proxy configuration with one or two relay hops.

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
init(relayHops: [ProxyConfiguration.RelayHop])
```

## Parameters

- `relayHops`: An array of relay hops, which must contain either one or two hops.

## See Also

- [ProxyConfiguration.RelayHop](proxyconfiguration/relayhop.md)
  A single relay server you can chain together with other servers.
- [init(httpCONNECTProxy: NWEndpoint, tlsOptions: NWProtocolTLS.Options?)](proxyconfiguration/init(httpconnectproxy:tlsoptions:).md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [init(socksv5Proxy: NWEndpoint)](proxyconfiguration/init(socksv5proxy:).md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration/init(relayhops:))*