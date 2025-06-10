# NetworkConnection

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
final class NetworkConnection<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Topics

### Classes
- [NetworkConnection.SubConnection](networkconnection/subconnection.md)
### Initializers
- [convenience init(to: NWEndpoint, using: () -> ApplicationProtocol)](networkconnection/init(to:using:)-182om.md)
- [convenience init(to: any Connectable, using: () -> ApplicationProtocol)](networkconnection/init(to:using:)-51aq2.md)
- [convenience init(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>)](networkconnection/init(to:using:)-5e864.md)
- [convenience init(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>)](networkconnection/init(to:using:)-69glf.md)
- [convenience init(to: any Connectable, using: NWParametersBuilder<ApplicationProtocol>)](networkconnection/init(to:using:)-6yzx9.md)
- [convenience init(to: any Connectable, using: () -> ApplicationProtocol)](networkconnection/init(to:using:)-7gprx.md)
- [convenience init(to: NWEndpoint, using: () -> ApplicationProtocol)](networkconnection/init(to:using:)-907m0.md)
- [convenience init(to: any Connectable, using: NWParametersBuilder<ApplicationProtocol>)](networkconnection/init(to:using:)-9kq3t.md)
### Instance Properties
- [var applicationError: NWProtocolQUIC.ApplicationError](networkconnection/applicationerror.md)
  The QUIC application error code to send for the connection, or received from the peer.
- [var currentPath: NWPath?](networkconnection/currentpath.md)
  Current path for the connection, which can be used to extract interface and effective endpoint information
- [var datagrams: NetworkConnection<QUIC>.SubConnection<QUICDatagram>](networkconnection/datagrams.md)
  Access a `SubConnection` object to send connection-wide unreliable datagrams over QUIC. Subsequent accesses to this object will return the same reference. All incoming datagrams for the entire QUIC connection will be received on this `SubConnection` once invoked.
- [var debugDescription: String](networkconnection/debugdescription.md)
- [var id: String](networkconnection/id.md)
- [var identifier: UInt64](networkconnection/identifier.md)
  An identifier representing the original connection for the multiplexed tunnel
- [var keepAlive: NWProtocolQUIC.Metadata.KeepAliveBehavior](networkconnection/keepalive.md)
  Set the QUIC connection keep-alive interval.
- [var localEndpoint: NWEndpoint?](networkconnection/localendpoint.md)
  The local endpoint of the connection
- [var maximumDatagramSize: Int](networkconnection/maximumdatagramsize.md)
  Retrieve the maximum datagram size that can be sent on the connection. Any datagrams sent should be less than or equal to this size.
- [var messages: AsyncThrowingStream<ApplicationProtocol.Message<ApplicationProtocol.Receiving>, any Error>](networkconnection/messages.md)
- [var negotiatedALPN: String?](networkconnection/negotiatedalpn.md)
  Return the negotiated application protocol used when establishing the connection
- [var parameters: NWParameters](networkconnection/parameters.md)
  The set of parameters with which the connection was created
- [var remoteEndpoint: NWEndpoint?](networkconnection/remoteendpoint.md)
  The remote endpoint of the connection
- [var remoteIdleTimeout: Int](networkconnection/remoteidletimeout.md)
  Access the idle_timeout value in milliseconds received from the peer in the transport parameters.
- [var remoteMaxStreamsBidirectional: Int](networkconnection/remotemaxstreamsbidirectional.md)
  Get the maximum number of bidirectional streams advertised by peer that an application is allowed to create.
- [var remoteMaxStreamsUnidirectional: Int](networkconnection/remotemaxstreamsunidirectional.md)
  Get the maximum number of unidirectional streams advertised by peer that an application is allowed to create.
- [var securityProtocolMetadata: sec_protocol_metadata_t](networkconnection/securityprotocolmetadata.md)
  Access the sec_protocol_metadata_t for the QUIC Connection. See <Security/SecProtocolMetadata.h> for functions to further access security metadata.
- [var state: NWConnection.State](networkconnection/state.md)
  Access the current state of the connection
- [var usableDatagramFrameSize: Int](networkconnection/usabledatagramframesize.md)
  Get the usable size of a datagram frame from a QUIC datagram flow.
### Instance Methods
- [func cancelCurrentEndpoint()](networkconnection/cancelcurrentendpoint.md)
  Cancel the currently connected endpoint, causing the connection to fall through to the next endpoint if available, or to go to the waiting state if no more endpoints are available.
- [func close(code: NWProtocolWebSocket.CloseCode, reason: String?, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/close(code:reason:metadata:).md)
- [func establishmentReport() async throws -> NWConnection.EstablishmentReport?](networkconnection/establishmentreport.md)
  Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, the report will be nil.
- [func hash(into: inout Hasher)](networkconnection/hash(into:).md)
- [func inboundStreams((NetworkConnection<QUIC>.SubConnection<QUICStream>) async throws -> Void) async throws](networkconnection/inboundstreams(_:).md)
  Handle inbound streams and provide a closure on which callback handlers will be executed. When the `NetworkConnection` state moves to `ready`, the internal listener is registered with the system and can receive incoming streams on the multiplexing instance. `inboundStreams` should only be called once on a `NetworkConnection`, and multiple calls to run will throw an exception.
- [func inboundStreams<NewApplicationProtocol>(prepending: () -> NewApplicationProtocol, (NetworkConnection<QUIC>.SubConnection<NewApplicationProtocol>) async throws -> Void) async throws](networkconnection/inboundstreams(prepending:_:).md)
  Handle inbound QUIC streams and provide a closure on which callback handlers will be executed. When the `NetworkConnection` state moves to `ready`, the internal listener is registered with the system and can receive incoming streams on the multiplexing instance. `inboundStreams` should only be called once on a `NetworkConnection`, and multiple calls to run will throw an exception.
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](networkconnection/metadata(definition:).md)
  Access connection-wide protocol metadata on the connection. This allows access to state for protocols like TCP and TLS that have long-term state.
- [func onBetterPathUpdate(((NetworkConnection<ApplicationProtocol>, Bool) -> Void)?) -> Self](networkconnection/onbetterpathupdate(_:).md)
- [func onPathUpdate(((NetworkConnection<ApplicationProtocol>, NWPath) -> Void)?) -> Self](networkconnection/onpathupdate(_:).md)
- [func onStateUpdate(((NetworkConnection<ApplicationProtocol>, NWConnection.State) -> Void)?) -> Self](networkconnection/onstateupdate(_:)-2xbqu.md)
- [func onStateUpdate(((NetworkConnection<ApplicationProtocol>, NWConnection.State) -> Void)?) -> Self](networkconnection/onstateupdate(_:)-4j4zj.md)
- [func onViabilityUpdate(((NetworkConnection<ApplicationProtocol>, Bool) -> Void)?) -> Self](networkconnection/onviabilityupdate(_:).md)
- [func openStream(directionality: QUICStream.Directionality) async throws -> NetworkConnection<QUIC>.SubConnection<QUICStream>](networkconnection/openstream(directionality:).md)
  Initiate a new data stream over QUIC. When invoked with no parameters, the default stream type will be bidirectional. Unidirectional streams can be initiated by setting the optional `bidirectional` parameter to false.
- [func openStream<NewApplicationProtocol>(directionality: QUICStream.Directionality, () -> NewApplicationProtocol) async throws -> NetworkConnection<QUIC>.SubConnection<NewApplicationProtocol>](networkconnection/openstream(directionality:_:).md)
  Initiate a new data stream over QUIC. When invoked with no parameters, the default stream type will be bidirectional. Unidirectional streams can be initiated by setting the optional `bidirectional` parameter to false.
- [func ping<Content>(Content?, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/ping(_:metadata:).md)
- [func pong<Content>(Content?, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/pong(_:metadata:).md)
- [func prependProtocols<NewApplicationProtocol>(() -> NewApplicationProtocol) -> NetworkConnection<NewApplicationProtocol>](networkconnection/prependprotocols(_:).md)
- [func receive() async throws -> ApplicationProtocol.Message<Data>](networkconnection/receive-3ne1p.md)
- [func receive() async throws -> ApplicationProtocol.Message<Data>](networkconnection/receive-4viq3.md)
- [func receive() async throws -> ApplicationProtocol.Message<Data>](networkconnection/receive-5snd0.md)
- [func receive<Sending, Receiving, CoderType>() async throws -> ApplicationProtocol.Message<Receiving>](networkconnection/receive-6ma5m.md)
- [func receive<Value>(as: Value.Type) async throws -> ApplicationProtocol.Message<Value>](networkconnection/receive(as:).md)
- [func receive(atLeast: Int, atMost: Int) async throws -> ApplicationProtocol.Message<Data>](networkconnection/receive(atleast:atmost:).md)
- [func receive(exactly: Int) async throws -> ApplicationProtocol.Message<Data>](networkconnection/receive(exactly:).md)
- [func send<Content>(Content, endOfStream: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/send(_:endofstream:metadata:)-4bcl8.md)
- [func send<Value>(Value, endOfStream: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/send(_:endofstream:metadata:)-4s98d.md)
- [func send<Content>(Content, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/send(_:metadata:)-1rzps.md)
- [func send<Content>(Content, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/send(_:metadata:)-4ittg.md)
- [func send<Sending, Receiving, CoderType>(Sending, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/send(_:metadata:)-7s776.md)
- [func send(String, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/send(_:metadata:)-g5jj.md)
- [func send<Content>(Content, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkconnection/send(_:type:lastmessage:metadata:).md)
- [func sendIdempotent<Value>(Value, endOfStream: Bool, metadata: () -> [NWProtocolMetadata])](networkconnection/sendidempotent(_:endofstream:metadata:)-1qjmd.md)
- [func sendIdempotent<Content>(Content, endOfStream: Bool, metadata: () -> [NWProtocolMetadata])](networkconnection/sendidempotent(_:endofstream:metadata:)-85rup.md)
- [func sendIdempotent<Content>(Content, metadata: () -> [NWProtocolMetadata])](networkconnection/sendidempotent(_:metadata:)-7gs9e.md)
- [func sendIdempotent(String, metadata: () -> [NWProtocolMetadata])](networkconnection/sendidempotent(_:metadata:)-9tocn.md)
- [func sendIdempotent<Content>(Content, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata])](networkconnection/sendidempotent(_:type:lastmessage:metadata:).md)
- [func start() -> Self](networkconnection/start.md)
  Initiate some action to open the connection on the network like making a handshake, initiating a multiplexing session, etc. Starts the connection, which will cause the connection to evaluate its path, do resolution, and try to become ready (connected). `NetworkConnection` establishment is asynchronous. `onStateUpdate` will be called when the state changes. If the connection cannot be established, the state will transition to `waiting` with an associated error describing the reason. If an unrecoverable error is encountered, the state will transition to `failed` with an associated error value. If the connection is established, the state will transition to `ready`.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](networkconnection/startdatatransferreport.md)
  Start a new pending data transfer report on a connection. Multiple reports may be created for a single NWConnection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last).
- [func startReceive(((Int, Int) async throws -> ApplicationProtocol.Message<Data>) async throws -> Void) async throws](networkconnection/startreceive(_:).md)
- [func startSend(String, metadata: () -> [NWProtocolMetadata], handler: ((String, Bool) async throws -> Void) async throws -> Void) async throws](networkconnection/startsend(_:metadata:handler:)-1w94c.md)
- [func startSend<Content>(Content, metadata: () -> [NWProtocolMetadata], handler: ((Content, Bool) async throws -> Void) async throws -> Void) async throws](networkconnection/startsend(_:metadata:handler:)-s99g.md)

## Relationships

### Conforms To
- [ConnectionProtocol](connectionprotocol.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection)*