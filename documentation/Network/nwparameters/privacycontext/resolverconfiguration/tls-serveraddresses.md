# NWParameters.PrivacyContext.ResolverConfiguration.tls(_:serverAddresses:)

**Framework**: Network  
**Kind**: case

A DNS-over-TLS resolver configuration.

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
case tls(NWEndpoint, serverAddresses: [NWEndpoint])
```

#### Discussion

The hostname of the provided endpoint will be used to validate the TLS certificate of the server. See [`RFC 7858`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7858) for more details. The associated server addresses you provide are hints for which well-known DNS server addresses to use.

## See Also

- [NWParameters.PrivacyContext.ResolverConfiguration.https(_:serverAddresses:)](nwparameters/privacycontext/resolverconfiguration/https(_:serveraddresses:).md)
  A DNS-over-HTTPS resolver configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/privacycontext/resolverconfiguration/tls(_:serveraddresses:))*