# NWProtocolUDP.Options

**Framework**: Network  
**Kind**: class

A container of options for configuring how UDP is used on a connection.

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

### Customizing UDP Connections
- [init()](nwprotocoludp/options/init.md)
  Initializes a default set of UDP connection options.
- [var preferNoChecksum: Bool](nwprotocoludp/options/prefernochecksum.md)
  A Boolean that configures the connection to not send UDP checksums.

## Relationships

### Inherits From
- [NWProtocolOptions](nwprotocoloptions.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let definition: NWProtocolDefinition](nwprotocoludp/definition.md)
  The system definition of the User Datagram Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoludp/options)*