# openStream(directionality:_:)

**Framework**: Network  
**Kind**: method

Initiate a new data stream over QUIC. When invoked with no parameters, the default stream type will be bidirectional. Unidirectional streams can be initiated by setting the optional `bidirectional` parameter to false.

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
final func openStream<NewApplicationProtocol>(directionality: QUICStream.Directionality = .bidirectional, @ProtocolStackBuilder<NewApplicationProtocol> _ prepending: (QUICStream) -> NewApplicationProtocol) async throws -> QUIC.Stream<NewApplicationProtocol> where NewApplicationProtocol : OneToOneProtocol
```

#### Discussion

This call will start the underlying QUIC connection if it has not been started already and will block until the QUIC connection is ready.

The passed protocols in the `prepending` ProtocolStackBuilder will be added on top of the created QUIC Stream.

While streams can be cancelled independently of the underlying connection, if the parent NetworkChannel is cancelled or fails, the streams will as well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/openstream(directionality:_:))*