# NWParameters.PrivacyContext.ResolverConfiguration

**Framework**: Network  
**Kind**: enum

A DNS server configuration that uses TLS or HTTPS.

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
enum ResolverConfiguration
```

## Topics

### Resolver Types
- [NWParameters.PrivacyContext.ResolverConfiguration.https(_:serverAddresses:)](nwparameters/privacycontext/resolverconfiguration/https(_:serveraddresses:).md)
  A DNS-over-HTTPS resolver configuration.
- [NWParameters.PrivacyContext.ResolverConfiguration.tls(_:serverAddresses:)](nwparameters/privacycontext/resolverconfiguration/tls(_:serveraddresses:).md)
  A DNS-over-TLS resolver configuration.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func requireEncryptedNameResolution(Bool, fallbackResolver: NWParameters.PrivacyContext.ResolverConfiguration?)](nwparameters/privacycontext/requireencryptednameresolution(_:fallbackresolver:).md)
  Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/privacycontext/resolverconfiguration)*