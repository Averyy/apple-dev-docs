# NetworkConnection.SubConnection

**Framework**: Network  
**Kind**: class

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
final class SubConnection<SubApplicationProtocol> where SubApplicationProtocol : OneToOneProtocol
```

## Topics

### Instance Properties
- [var directionality: QUICStream.Directionality](networkconnection/subconnection/directionality.md)
  The directionality of this stream, either bidirectional or unidirectional.
- [var initiator: QUICStream.Initiator](networkconnection/subconnection/initiator.md)
  The initiator of this QUIC stream, either client or server.
- [var messages: AsyncThrowingStream<SubApplicationProtocol.Message<SubApplicationProtocol.Receiving>, any Error>](networkconnection/subconnection/messages.md)
- [var streamApplicationErrorCode: UInt64](networkconnection/subconnection/streamapplicationerrorcode.md)
  The QUIC application error code to send for the stream, or received from the peer.
- [var streamID: UInt64](networkconnection/subconnection/streamid.md)
  The QUIC stream identifier.
### Instance Methods
- [func close(code: NWProtocolWebSocket.CloseCode, reason: String?, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/close(code:reason:metadata:).md)
- [func onBetterPathUpdate(((NetworkConnection<ApplicationProtocol>.SubConnection<SubApplicationProtocol>, Bool) -> Void)?) -> Self](networkconnection/subconnection/onbetterpathupdate(_:).md)
- [func onPathUpdate(((NetworkConnection<ApplicationProtocol>.SubConnection<SubApplicationProtocol>, NWPath) -> Void)?) -> Self](networkconnection/subconnection/onpathupdate(_:).md)
- [func onStateUpdate(((NetworkConnection<ApplicationProtocol>.SubConnection<SubApplicationProtocol>, NWConnection.State) -> Void)?) -> Self](networkconnection/subconnection/onstateupdate(_:).md)
- [func onViabilityUpdate(((NetworkConnection<ApplicationProtocol>.SubConnection<SubApplicationProtocol>, Bool) -> Void)?) -> Self](networkconnection/subconnection/onviabilityupdate(_:).md)
- [func ping(Data?, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/ping(_:metadata:).md)
- [func pong(Data?, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/pong(_:metadata:).md)
- [func prependProtocols<NewSubApplicationProtocol>(() -> NewSubApplicationProtocol) -> NetworkConnection<ApplicationProtocol>.SubConnection<NewSubApplicationProtocol>](networkconnection/subconnection/prependprotocols(_:).md)
- [func receive() async throws -> SubApplicationProtocol.Message<Data>](networkconnection/subconnection/receive-4kzlp.md)
- [func receive() async throws -> SubApplicationProtocol.Message<Data>](networkconnection/subconnection/receive-4ze8z.md)
- [func receive<Sending, Receiving, CoderType>() async throws -> SubApplicationProtocol.Message<Receiving>](networkconnection/subconnection/receive-55nuc.md)
- [func receive() async throws -> SubApplicationProtocol.Message<Data>](networkconnection/subconnection/receive-6pqg5.md)
- [func receive() async throws -> SubApplicationProtocol.Message<Data>](networkconnection/subconnection/receive-9h1vs.md)
- [func receive(atLeast: Int, atMost: Int) async throws -> SubApplicationProtocol.Message<Data>](networkconnection/subconnection/receive(atleast:atmost:).md)
- [func receive(exactly: Int) async throws -> SubApplicationProtocol.Message<Data>](networkconnection/subconnection/receive(exactly:).md)
- [func send(Data, endOfStream: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/send(_:endofstream:metadata:).md)
- [func send(Data, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/send(_:metadata:)-39f9s.md)
- [func send(String, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/send(_:metadata:)-5wons.md)
- [func send<Sending, Receiving, CoderType>(Sending, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/send(_:metadata:)-60h4k.md)
- [func send(Data, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/send(_:metadata:)-6uv1n.md)
- [func send(Data, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/send(_:metadata:)-7nf9t.md)
- [func send(Data, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/subconnection/send(_:type:lastmessage:metadata:).md)
- [func sendIdempotent(Data, endOfStream: Bool, metadata: () -> [NWProtocolMetadata])](networkconnection/subconnection/sendidempotent(_:endofstream:metadata:).md)
- [func sendIdempotent(Data, metadata: () -> [NWProtocolMetadata])](networkconnection/subconnection/sendidempotent(_:metadata:)-8yrvp.md)
- [func sendIdempotent(String, metadata: () -> [NWProtocolMetadata])](networkconnection/subconnection/sendidempotent(_:metadata:)-mtat.md)
- [func sendIdempotent(Data, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata])](networkconnection/subconnection/sendidempotent(_:type:lastmessage:metadata:).md)
- [func startReceive(((Int, Int) async throws -> SubApplicationProtocol.Message<Data>) async throws -> Void) async throws](networkconnection/subconnection/startreceive(_:).md)
- [func startSend(Data, metadata: () -> [NWProtocolMetadata], handler: ((Data, Bool) async throws -> Void) async throws -> Void) async throws](networkconnection/subconnection/startsend(_:metadata:handler:)-1e1o9.md)
- [func startSend(String, metadata: () -> [NWProtocolMetadata], handler: ((String, Bool) async throws -> Void) async throws -> Void) async throws](networkconnection/subconnection/startsend(_:metadata:handler:)-3ewbg.md)

## Relationships

### Conforms To
- [ConnectionProtocol](connectionprotocol.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SubConnectionProtocol](subconnectionprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/subconnection)*