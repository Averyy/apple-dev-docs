# openStream(directionality:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

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
final func openStream(directionality: QUICStream.Directionality = .bidirectional) async throws -> QUIC.Stream<QUICStream>
```

Available when `ApplicationProtocol` is `QUIC`.

## Discussion

This call will start the underlying QUIC connection if it has not been started already and will block until the QUIC connection is ready.

While streams can be cancelled independently of the underlying connection, if the parent NetworkChannel is cancelled or fails, the streams will as well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/openstream(directionality:))*