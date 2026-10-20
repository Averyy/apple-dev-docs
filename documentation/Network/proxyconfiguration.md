# ProxyConfiguration

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

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
struct ProxyConfiguration
```

## Topics

### Creating Proxy Configurations
- [init(relayHops: [ProxyConfiguration.RelayHop])](./proxyconfiguration/init%28relayhops%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [ProxyConfiguration.RelayHop](./proxyconfiguration/relayhop.md)
  A single relay server you can chain together with other servers.
- [init(httpCONNECTProxy: NWEndpoint, tlsOptions: NWProtocolTLS.Options?)](./proxyconfiguration/init%28httpconnectproxy,tlsoptions%29.md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [init(socksv5Proxy: NWEndpoint)](./proxyconfiguration/init%28socksv5proxy%29.md)
  Initializes a SOCKSv5 proxy configuration.
### Customizing Proxy Behavior
- [var allowFailover: Bool](./proxyconfiguration/allowfailover.md)
  A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.
- [func applyCredential(username: String, password: String)](./proxyconfiguration/applycredential%28username,password%29.md)
  Sets a username and password to use as authentication for a proxy configuration.
### Initializers
- [init(obliviousHTTPRelay: ProxyConfiguration.RelayHop, relayResourcePath: String, gatewayKeyConfig: Data, matchDomains: [String])](./proxyconfiguration/init%28oblivioushttprelay,relayresourcepath,gatewaykeyconfig,matchdomains%29.md)
### Instance Properties
- [var excludedDomains: [String]](./proxyconfiguration/excludeddomains.md)
- [var matchDomains: [String]](./proxyconfiguration/matchdomains.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring Proxies
- [var proxyConfigurations: [ProxyConfiguration]](./nwparameters/privacycontext/proxyconfigurations.md)
  Applies proxy configurations for all connections associated with this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/proxyconfiguration)*