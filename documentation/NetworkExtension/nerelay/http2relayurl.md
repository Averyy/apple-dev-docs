# http2RelayURL

**Framework**: Network Extension  
**Kind**: property

A URL identifying the relay server accessible using HTTP/2.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var http2RelayURL: URL? { get set }
```

## See Also

- [var http3RelayURL: URL?](nerelay/http3relayurl.md)
  A URL identifying the relay server accessible using HTTP/3.
- [var dnsOverHTTPSURL: URL?](nerelay/dnsoverhttpsurl.md)
  The URL of a DNS-over-HTTPS (DoH) resolver accessible from the relay.
- [var rawPublicKeys: [Data]?](nerelay/rawpublickeys.md)
  An array of TLS raw public keys that the relay server can present during the TLS handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelay/http2relayurl)*