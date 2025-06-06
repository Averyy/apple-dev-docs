# NWProtocol

**Framework**: Network  
**Kind**: class

The abstract superclass used by Network framework protocols and by custom network protocols that you define.

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
class NWProtocol
```

## Topics

### Adding Protocols to Connections
- [class NWProtocolOptions](nwprotocoloptions.md)
  The abstract superclass for configuring the options of a network protocol.
- [class NWProtocolDefinition](nwprotocoldefinition.md)
  The abstract superclass for identifying a network protocol.
### Interacting with Protocols
- [class NWProtocolMetadata](nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.

## Relationships

### Inherited By
- [NWProtocolFramer](nwprotocolframer.md)
- [NWProtocolIP](nwprotocolip.md)
- [NWProtocolQUIC](nwprotocolquic.md)
- [NWProtocolTCP](nwprotocoltcp.md)
- [NWProtocolTLS](nwprotocoltls.md)
- [NWProtocolUDP](nwprotocoludp.md)
- [NWProtocolWebSocket](nwprotocolwebsocket.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var defaultProtocolStack: NWParameters.ProtocolStack](nwparameters/defaultprotocolstack.md)
  The protocol stack used by connections and listeners.
- [NWParameters.ProtocolStack](nwparameters/protocolstack.md)
  An ordered set of protocol options that define the protocols that connections and listeners use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocol)*