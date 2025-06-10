# NWProtocolTLS.Options

**Framework**: Network  
**Kind**: class

A container of options for configuring how TLS is used on a connection.

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
class Options
```

## Topics

### Customizing TLS Connections
- [init()](nwprotocoltls/options/init.md)
  Initializes a default set of TLS connection options.
- [var securityProtocolOptions: sec_protocol_options_t](nwprotocoltls/options/securityprotocoloptions.md)
  The handshake security options TLS uses.

## Relationships

### Inherits From
- [NWProtocolOptions](nwprotocoloptions.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let definition: NWProtocolDefinition](nwprotocoltls/definition.md)
  The system definition of the Transport Layer Security protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltls/options)*