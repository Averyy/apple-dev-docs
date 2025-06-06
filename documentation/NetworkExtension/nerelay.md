# NERelay

**Framework**: Network Extension  
**Kind**: class

A single relay server configuration that you can chain together with other relays.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NERelay
```

#### Overview

Relay servers are secure HTTP proxies that allow proxying TCP traffic using the `CONNECT` method and UDP traffic using the `connect-udp` protocol defined in [`RFC 9298`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc9298.html).

## Topics

### Configuring server properties
- [var http3RelayURL: URL?](nerelay/http3relayurl.md)
  A URL identifying the relay server accessible using HTTP/3.
- [var http2RelayURL: URL?](nerelay/http2relayurl.md)
  A URL identifying the relay server accessible using HTTP/2.
- [var dnsOverHTTPSURL: URL?](nerelay/dnsoverhttpsurl.md)
  The URL of a DNS-over-HTTPS (DoH) resolver accessible from the relay.
- [var rawPublicKeys: [Data]?](nerelay/rawpublickeys.md)
  An array of TLS raw public keys that the relay server can present during the TLS handshake.
### Configuring client properties
- [var additionalHTTPHeaderFields: [String : String]](nerelay/additionalhttpheaderfields.md)
  A dictionary of additional HTTP headers to send as part of `CONNECT` requests to the relay.
- [var identityData: Data?](nerelay/identitydata.md)
  The PKCS12 data for the relay client authentication.
- [var identityDataPassword: String?](nerelay/identitydatapassword.md)
  The password the relay uses to decrypt the PKCS12 identity data.
- [var syntheticDNSAnswerIPv4Prefix: String?](nerelay/syntheticdnsansweripv4prefix.md)
  An IPv4 address prefix the relay uses to handle address info requests.
- [var syntheticDNSAnswerIPv6Prefix: String?](nerelay/syntheticdnsansweripv6prefix.md)
  An IPv6 address prefix the relay uses to handle address info requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NERelayManager](nerelaymanager.md)
  An object you use to create and manage a network relay configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelay)*