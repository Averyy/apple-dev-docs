# NWParameters.PrivacyContext.ResolverConfiguration.https(_:serverAddresses:)

**Framework**: Network  
**Kind**: case

A DNS-over-HTTPS resolver configuration.

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
case https(URL, serverAddresses: [NWEndpoint])
```

#### Discussion

The URL describes the location of the DNS server, such as “https://dnsserver.example.net/dns-query”. See [`RFC 8484`](https://developer.apple.comhttps://tools.ietf.org/html/rfc8484) for more details. The associated server addresses you provide are hints for which well-known DNS server addresses to use.

## See Also

- [NWParameters.PrivacyContext.ResolverConfiguration.tls(_:serverAddresses:)](nwparameters/privacycontext/resolverconfiguration/tls(_:serveraddresses:).md)
  A DNS-over-TLS resolver configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/privacycontext/resolverconfiguration/https(_:serveraddresses:))*