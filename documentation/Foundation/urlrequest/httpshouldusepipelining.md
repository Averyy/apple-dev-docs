# httpShouldUsePipelining

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the request should transmit before the previous response is received.

**Availability**:
- iOS 8.0+ - Deprecated in 18.4
- iPadOS 8.0+ - Deprecated in 18.4
- Mac Catalyst 8.0+ - Deprecated in 18.4
- macOS 10.10+ - Deprecated in 15.4
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 2.0+ - Deprecated in 11.4

> **Deprecated**: Pipelining is an HTTP/1.1 concept. Adopt HTTP/2 or later instead.

## Declaration

```swift
var httpShouldUsePipelining: Bool { get set }
```

#### Discussion

HTTP/2 and later ignore this property. HTTP/1.1 only considers this property in the classic loading mode (`usesClassicLoadingMode`).

## See Also

### Controlling request behavior
- [var timeoutInterval: TimeInterval](./timeoutinterval.md)
  The timeout interval of the request.
- [var httpShouldHandleCookies: Bool](./httpshouldhandlecookies.md)
  A Boolean value indicating whether cookies will be sent with and set for this request.
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.
- [var allowsPersistentDNS: Bool](./allowspersistentdns.md)
  `true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.
- [var assumesHTTP3Capable: Bool](./assumeshttp3capable.md)
  `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [var cookiePartitionIdentifier: String?](./cookiepartitionidentifier.md)
- [var requiresDNSSECValidation: Bool](./requiresdnssecvalidation.md)
  `true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/httpshouldusepipelining)*