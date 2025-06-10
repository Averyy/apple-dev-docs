# openStream(directionality:_:)

**Framework**: Network  
**Kind**: method

Initiate a new data stream over QUIC. When invoked with no parameters, the default stream type will be bidirectional. Unidirectional streams can be initiated by setting the optional `bidirectional` parameter to false.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final func openStream<NewApplicationProtocol>(directionality: QUICStream.Directionality = .bidirectional, @ProtocolStackBuilder<NewApplicationProtocol> _ prepending: () -> NewApplicationProtocol) async throws -> NetworkConnection<QUIC>.SubConnection<NewApplicationProtocol> where NewApplicationProtocol : OneToOneProtocol
```

#### Discussion

This call will start the underlying QUIC connection if it has not been started already and will block until the QUIC connection is ready.

The passed protocols in the `prepending` ProtocolStackBuilder will be added on top of the created QUIC Stream.

While streams can be cancelled independently of the underlying connection, if the parent NetworkConnection is cancelled or fails, the streams will as well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/openstream(directionality:_:))*