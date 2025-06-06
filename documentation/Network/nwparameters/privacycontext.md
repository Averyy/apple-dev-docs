# NWParameters.PrivacyContext

**Framework**: Network  
**Kind**: class

An object that defines the privacy requirements for a set of connections.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class PrivacyContext
```

## Topics

### Configuring Custom Privacy Settings
- [init(description: String)](nwparameters/privacycontext/init(description:).md)
  Initializes a privacy context with a description string.
- [static let `default`: NWParameters.PrivacyContext](nwparameters/privacycontext/default.md)
  The privacy context that applies to all connections that do not use a custom context.
- [func disableLogging()](nwparameters/privacycontext/disablelogging.md)
  Disables system logging of connection activity.
- [func flushCache()](nwparameters/privacycontext/flushcache.md)
  Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.
### Requiring Encrypted DNS
- [func requireEncryptedNameResolution(Bool, fallbackResolver: NWParameters.PrivacyContext.ResolverConfiguration?)](nwparameters/privacycontext/requireencryptednameresolution(_:fallbackresolver:).md)
  Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
- [NWParameters.PrivacyContext.ResolverConfiguration](nwparameters/privacycontext/resolverconfiguration.md)
  A DNS server configuration that uses TLS or HTTPS.
### Configuring Proxies
- [var proxyConfigurations: [ProxyConfiguration]](nwparameters/privacycontext/proxyconfigurations.md)
  Applies proxy configurations for all connections associated with this context.
- [struct ProxyConfiguration](proxyconfiguration.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setPrivacyContext(NWParameters.PrivacyContext)](nwparameters/setprivacycontext(_:).md)
  Associates a privacy context with any connections or listeners that use the parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/privacycontext)*