# NWEndpoint.Port

**Framework**: Network  
**Kind**: struct

A port number you use along with a host to identify a network endpoint.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct Port
```

## Topics

### Creating Ports
- [init?(String)](nwendpoint/port/init(_:).md)
  Initializes a port with a string.
### Setting Well-Known Ports
- [static let any: NWEndpoint.Port](nwendpoint/port/any.md)
  The unspecified port (port 0).
- [static let ssh: NWEndpoint.Port](nwendpoint/port/ssh.md)
  The Secure Shell port (port 22).
- [static let smtp: NWEndpoint.Port](nwendpoint/port/smtp.md)
  The Simple Mail Transfer Protocol port (port 25).
- [static let http: NWEndpoint.Port](nwendpoint/port/http.md)
  The Hypertext Transfer Protocol port (port 80).
- [static let pop: NWEndpoint.Port](nwendpoint/port/pop.md)
  The Post Office Protocol port (port 110).
- [static let imap: NWEndpoint.Port](nwendpoint/port/imap.md)
  The Internet Message Access Protocol port (port 143).
- [static let https: NWEndpoint.Port](nwendpoint/port/https.md)
  The Secure Hypertext Transfer Protocol port (port 443).
- [static let imaps: NWEndpoint.Port](nwendpoint/port/imaps.md)
  The Secure Internet Message Access Protocol port (port 993).
- [static let socks: NWEndpoint.Port](nwendpoint/port/socks.md)
  The SOCKS proxy protocol port (port 1080).

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NWEndpoint.Host](nwendpoint/host.md)
  A name or address that identifies a network endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/port)*