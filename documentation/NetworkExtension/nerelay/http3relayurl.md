# http3RelayURL

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A URL identifying the relay server accessible using HTTP/3.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var http3RelayURL: URL? { get set }
```

```objc
@property (copy, nullable) NSURL * HTTP3RelayURL;
```

## See Also

### Configuring server properties
- [var http2RelayURL: URL?](./http2relayurl.md)
  A URL identifying the relay server accessible using HTTP/2.
- [var dnsOverHTTPSURL: URL?](./dnsoverhttpsurl.md)
  The URL of a DNS-over-HTTPS (DoH) resolver accessible from the relay.
- [var rawPublicKeys: [Data]?](./rawpublickeys.md)
  An array of TLS raw public keys that the relay server can present during the TLS handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelay/http3relayurl)*