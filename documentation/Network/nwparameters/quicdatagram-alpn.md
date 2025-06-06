# quicDatagram(alpn:)

**Framework**: Network  
**Kind**: method

Returns a set of default parameters for connections and listeners that use QUIC datagrams, with a set of supported Application-Layer Protocol Negotiation values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final class func quicDatagram(alpn: [String]) -> NWParameters
```

## Parameters

- `alpn`: A set of supported Application-Layer Protocol Negotiation values.

## See Also

- [class var tls: NWParameters](nwparameters/tls.md)
  A set of default parameters for connections and listeners that use TLS and TCP.
- [class var tcp: NWParameters](nwparameters/tcp.md)
  A set of default parameters for connections and listeners that use TCP.
- [class var dtls: NWParameters](nwparameters/dtls.md)
  A set of default parameters for connections and listeners that use DTLS and UDP.
- [class var udp: NWParameters](nwparameters/udp.md)
  A set of default parameters for connections and listeners that use UDP.
- [class func quic(alpn: [String]) -> NWParameters](nwparameters/quic(alpn:).md)
  Returns a set of default parameters for connections and listeners that use QUIC, with a set of supported Application-Layer Protocol Negotiation values.
- [convenience init(tls: NWProtocolTLS.Options?, tcp: NWProtocolTCP.Options)](nwparameters/init(tls:tcp:).md)
  Initializes parameters for TLS connections and listeners with custom TLS and TCP options.
- [convenience init(dtls: NWProtocolTLS.Options?, udp: NWProtocolUDP.Options)](nwparameters/init(dtls:udp:).md)
  Initializes parameters for DTLS connections and listeners with custom DTLS and UDP options.
- [convenience init(quic: NWProtocolQUIC.Options)](nwparameters/init(quic:).md)
  Initializes parameters for QUIC connections and listeners with custom QUIC options.
- [init()](nwparameters/init.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [init(customIPProtocolNumber: UInt8)](nwparameters/init(customipprotocolnumber:).md)
  Initializes parameters for connections and listeners using a custom IP protocol.
- [func copy() -> NWParameters](nwparameters/copy.md)
  Performs a deep copy of a parameters object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/quicdatagram(alpn:))*