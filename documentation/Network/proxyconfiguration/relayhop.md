# ProxyConfiguration.RelayHop

**Framework**: Network  
**Kind**: struct

A single relay server you can chain together with other servers.

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
struct RelayHop
```

#### Overview

Relay servers are secure HTTP proxies that allow proxying TCP traffic using the `CONNECT` method and UDP traffic using the `connect-udp` protocol defined in [`RFC 9298`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc9298.html).

## Topics

### Creating Relay Hops
- [init(http3RelayEndpoint: NWEndpoint, http2RelayEndpoint: NWEndpoint?, tlsOptions: NWProtocolTLS.Options, additionalHTTPHeaderFields: [String : String])](proxyconfiguration/relayhop/init(http3relayendpoint:http2relayendpoint:tlsoptions:additionalhttpheaderfields:).md)
  Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.
- [init(http2RelayEndpoint: NWEndpoint, tlsOptions: NWProtocolTLS.Options, additionalHTTPHeaderFields: [String : String])](proxyconfiguration/relayhop/init(http2relayendpoint:tlsoptions:additionalhttpheaderfields:).md)
  Creates a configuration for a secure relay accessible only using HTTP/2.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(relayHops: [ProxyConfiguration.RelayHop])](proxyconfiguration/init(relayhops:).md)
  Initializes a proxy configuration with one or two relay hops.
- [init(httpCONNECTProxy: NWEndpoint, tlsOptions: NWProtocolTLS.Options?)](proxyconfiguration/init(httpconnectproxy:tlsoptions:).md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [init(socksv5Proxy: NWEndpoint)](proxyconfiguration/init(socksv5proxy:).md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration/relayhop)*