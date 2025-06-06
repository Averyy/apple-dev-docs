# NWProtocolMetadata

**Framework**: Network  
**Kind**: class

The abstract superclass for specifying metadata about a network protocol.

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
class NWProtocolMetadata
```

#### Overview

You can use metadata when sending and receiving messages, as well as when inspecting connection properties.

## Relationships

### Inherited By
- [NWProtocolFramer.Message](nwprotocolframer/message.md)
- [NWProtocolIP.Metadata](nwprotocolip/metadata.md)
- [NWProtocolQUIC.Metadata](nwprotocolquic/metadata.md)
- [NWProtocolTCP.Metadata](nwprotocoltcp/metadata.md)
- [NWProtocolTLS.Metadata](nwprotocoltls/metadata.md)
- [NWProtocolUDP.Metadata](nwprotocoludp/metadata.md)
- [NWProtocolWebSocket.Metadata](nwprotocolwebsocket/metadata.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](nwconnection/metadata(definition:).md)
  Retrieves the connection-wide metadata for a specific protocol.
- [let endpoint: NWEndpoint](nwconnection/endpoint.md)
  The remote endpoint with which the connection was initialized.
- [let parameters: NWParameters](nwconnection/parameters.md)
  The parameters with which the connection was initialized.
- [var queue: DispatchQueue?](nwconnection/queue.md)
  The queue on which connection events are delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolmetadata)*