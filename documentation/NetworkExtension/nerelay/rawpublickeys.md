# rawPublicKeys

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An array of TLS raw public keys that the relay server can present during the TLS handshake.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var rawPublicKeys: [Data]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSData *> * rawPublicKeys;
```

## Discussion

If you set one or more keys, the raw public keys are used to authenticate the relay server. If no keys are set, or if the array is `nil`, default TLS server certificate evaluation is used.

## See Also

### Configuring server properties
- [var http3RelayURL: URL?](./http3relayurl.md)
  A URL identifying the relay server accessible using HTTP/3.
- [var http2RelayURL: URL?](./http2relayurl.md)
  A URL identifying the relay server accessible using HTTP/2.
- [var dnsOverHTTPSURL: URL?](./dnsoverhttpsurl.md)
  The URL of a DNS-over-HTTPS (DoH) resolver accessible from the relay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelay/rawpublickeys)*