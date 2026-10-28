# ProxyConfiguration.RelayHop

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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

## Overview

Relay servers are secure HTTP proxies that allow proxying TCP traffic using the `CONNECT` method and UDP traffic using the `connect-udp` protocol defined in [RFC 9298](https://www.rfc-editor.org/rfc/rfc9298.html).

## Topics

### Creating Relay Hops
- [init(http3RelayEndpoint: NWEndpoint, http2RelayEndpoint: NWEndpoint?, tlsOptions: NWProtocolTLS.Options, additionalHTTPHeaderFields: [String : String])](./relayhop/init%28http3relayendpoint,http2relayendpoint,tlsoptions,additionalhttpheaderfields%29.md)
  Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.
- [init(http2RelayEndpoint: NWEndpoint, tlsOptions: NWProtocolTLS.Options, additionalHTTPHeaderFields: [String : String])](./relayhop/init%28http2relayendpoint,tlsoptions,additionalhttpheaderfields%29.md)
  Creates a configuration for a secure relay accessible only using HTTP/2.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating Proxy Configurations
- [init(relayHops: [ProxyConfiguration.RelayHop])](./init%28relayhops%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [init(httpCONNECTProxy: NWEndpoint, tlsOptions: NWProtocolTLS.Options?)](./init%28httpconnectproxy,tlsoptions%29.md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [init(socksv5Proxy: NWEndpoint)](./init%28socksv5proxy%29.md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration/relayhop)*