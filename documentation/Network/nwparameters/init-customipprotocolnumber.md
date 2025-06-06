# init(customIPProtocolNumber:)

**Framework**: Network  
**Kind**: init

Initializes parameters for connections and listeners using a custom IP protocol.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(customIPProtocolNumber: UInt8)
```

#### Discussion

Creating custom IP protocol connections requires the “com.apple.developer.networking.custom-protocol” entitlement.

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
- [convenience init(quic: NWProtocolQUIC.Options)](nwparameters/init(quic:).md)
  Initializes parameters for QUIC connections and listeners with custom QUIC options.
- [init()](nwparameters/init.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [func copy() -> NWParameters](nwparameters/copy.md)
  Performs a deep copy of a parameters object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/init(customipprotocolnumber:))*