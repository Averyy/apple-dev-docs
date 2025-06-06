# init(quic:)

**Framework**: Network  
**Kind**: init

Initializes parameters for QUIC connections and listeners with custom QUIC options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(quic: NWProtocolQUIC.Options)
```

## Parameters

- `quic`: A QUIC options instance.

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
- [class func quicDatagram(alpn: [String]) -> NWParameters](nwparameters/quicdatagram(alpn:).md)
  Returns a set of default parameters for connections and listeners that use QUIC datagrams, with a set of supported Application-Layer Protocol Negotiation values.
- [convenience init(tls: NWProtocolTLS.Options?, tcp: NWProtocolTCP.Options)](nwparameters/init(tls:tcp:).md)
  Initializes parameters for TLS connections and listeners with custom TLS and TCP options.
- [convenience init(dtls: NWProtocolTLS.Options?, udp: NWProtocolUDP.Options)](nwparameters/init(dtls:udp:).md)
  Initializes parameters for DTLS connections and listeners with custom DTLS and UDP options.
- [init()](nwparameters/init.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [init(customIPProtocolNumber: UInt8)](nwparameters/init(customipprotocolnumber:).md)
  Initializes parameters for connections and listeners using a custom IP protocol.
- [func copy() -> NWParameters](nwparameters/copy.md)
  Performs a deep copy of a parameters object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/init(quic:))*