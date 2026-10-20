# NWProtocolQUIC.Options.Direction

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

A directionality of a QUIC stream.

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
enum Direction
```

## Topics

### Direction Values
- [NWProtocolQUIC.Options.Direction.bidirectional](./direction-swift.enum/bidirectional.md)
  A bidirectional QUIC stream.
- [NWProtocolQUIC.Options.Direction.unidirectional](./direction-swift.enum/unidirectional.md)
  A unidirectional QUIC stream.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Customizing Stream Options
- [var direction: NWProtocolQUIC.Options.Direction](./direction-swift.property.md)
  The direction of the QUIC stream.
- [var isDatagram: Bool](./isdatagram.md)
  A Boolean that indicates that this is a QUIC datagram flow, not a stream of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/options/direction-swift.enum)*