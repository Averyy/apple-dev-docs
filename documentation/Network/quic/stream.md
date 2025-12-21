# QUIC.Stream

**Framework**: Network  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final class Stream<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Topics

### Instance Properties
- [var directionality: QUICStream.Directionality](quic/stream/directionality.md)
  The directionality of this stream, either bidirectional or unidirectional.
- [var initiator: QUICStream.Initiator](quic/stream/initiator.md)
  The initiator of this QUIC stream, either client or server.
- [let parent: NetworkConnection<QUIC>](quic/stream/parent.md)
- [var streamApplicationErrorCode: UInt64](quic/stream/streamapplicationerrorcode.md)
  The QUIC application error code to send for the stream, or received from the peer.
- [var streamID: UInt64](quic/stream/streamid.md)
  The QUIC stream identifier.

## Relationships

### Inherits From
- [NetworkChannel](networkchannel.md)
### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic/stream)*