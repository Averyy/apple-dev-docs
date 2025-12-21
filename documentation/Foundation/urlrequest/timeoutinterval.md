# timeoutInterval

**Framework**: Foundation  
**Kind**: property

The timeout interval of the request.

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
var timeoutInterval: TimeInterval { get set }
```

#### Discussion

If during a connection attempt the request remains idle for longer than the timeout interval, the request is considered to have timed out. The default timeout interval is 60 seconds.

As a general rule, you should not use short timeout intervals. Instead, you should provide an easy way for the user to cancel a long-running operation. For more information, read [`Designing for Real-World Networks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/WhyNetworkingIsHard/WhyNetworkingIsHard.html#//apple_ref/doc/uid/TP40010220-CH13) in [`Networking Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010220).

## See Also

- [var httpShouldHandleCookies: Bool](urlrequest/httpshouldhandlecookies.md)
  A Boolean value indicating whether cookies will be sent with and set for this request.
- [var httpShouldUsePipelining: Bool](urlrequest/httpshouldusepipelining.md)
  A Boolean value indicating whether the request should transmit before the previous response is received.
- [var allowsCellularAccess: Bool](urlrequest/allowscellularaccess.md)
  A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.
- [var allowsPersistentDNS: Bool](urlrequest/allowspersistentdns.md)
  `true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.
- [var assumesHTTP3Capable: Bool](urlrequest/assumeshttp3capable.md)
  `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [var cookiePartitionIdentifier: String?](urlrequest/cookiepartitionidentifier.md)
- [var requiresDNSSECValidation: Bool](urlrequest/requiresdnssecvalidation.md)
  `true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/timeoutinterval)*