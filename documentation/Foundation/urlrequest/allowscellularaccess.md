# allowsCellularAccess

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var allowsCellularAccess: Bool { get set }
```

#### Discussion

Setting this property to `true` makes the request eligible to run over cellular, subject to other considerations (including, but not limited to, the [`URLSessionConfiguration`](urlsessionconfiguration.md)’s [`allowsCellularAccess`](urlsessionconfiguration/allowscellularaccess.md) property). Setting this value to `false` ensures that the request will never run over cellular.

## See Also

- [var waitsForConnectivity: Bool](urlsessionconfiguration/waitsforconnectivity.md)
  A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [var timeoutInterval: TimeInterval](urlrequest/timeoutinterval.md)
  The timeout interval of the request.
- [var httpShouldHandleCookies: Bool](urlrequest/httpshouldhandlecookies.md)
  A Boolean value indicating whether cookies will be sent with and set for this request.
- [var httpShouldUsePipelining: Bool](urlrequest/httpshouldusepipelining.md)
  A Boolean value indicating whether the request should transmit before the previous response is received.
- [var allowsPersistentDNS: Bool](urlrequest/allowspersistentdns.md)
  `true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.
- [var assumesHTTP3Capable: Bool](urlrequest/assumeshttp3capable.md)
  `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [var cookiePartitionIdentifier: String?](urlrequest/cookiepartitionidentifier.md)
- [var requiresDNSSECValidation: Bool](urlrequest/requiresdnssecvalidation.md)
  `true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/allowscellularaccess)*