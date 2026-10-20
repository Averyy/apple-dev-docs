# NWEndpoint.Port

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [init?(String)](./port/init%28_%29.md)
  Initializes a port with a string.
### Setting Well-Known Ports
- [static let any: NWEndpoint.Port](./port/any.md)
  The unspecified port (port 0).
- [static let ssh: NWEndpoint.Port](./port/ssh.md)
  The Secure Shell port (port 22).
- [static let smtp: NWEndpoint.Port](./port/smtp.md)
  The Simple Mail Transfer Protocol port (port 25).
- [static let http: NWEndpoint.Port](./port/http.md)
  The Hypertext Transfer Protocol port (port 80).
- [static let pop: NWEndpoint.Port](./port/pop.md)
  The Post Office Protocol port (port 110).
- [static let imap: NWEndpoint.Port](./port/imap.md)
  The Internet Message Access Protocol port (port 143).
- [static let https: NWEndpoint.Port](./port/https.md)
  The Secure Hypertext Transfer Protocol port (port 443).
- [static let imaps: NWEndpoint.Port](./port/imaps.md)
  The Secure Internet Message Access Protocol port (port 993).
- [static let socks: NWEndpoint.Port](./port/socks.md)
  The SOCKS proxy protocol port (port 1080).

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByIntegerLiteral](../../Swift/expressiblebyintegerliteral.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Host and Ports
- [NWEndpoint.Host](./host.md)
  A name or address that identifies a network endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/port)*