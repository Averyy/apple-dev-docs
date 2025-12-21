# NetworkChannel

**Framework**: Network  
**Kind**: class

A base class supporting sending and recieving data through an arbitrary network channel.

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
class NetworkChannel<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

#### Overview

The interface exposed by this type (and any derived classes) is dependent on the generic ApplicationProtocol parameter.

## Topics

### Operators
- [static func == (NetworkChannel<ApplicationProtocol>, NetworkChannel<ApplicationProtocol>) -> Bool](networkchannel/==(_:_:).md)
  Compare two instances of NetworkChannel for equality
### Instance Properties
- [var debugDescription: String](networkchannel/debugdescription.md)
  Generate a string representation of NetworkChannel suitable for logging
- [var id: String](networkchannel/id.md)
  The stable identity of the entity associated with this instance.
- [var maximumDatagramSize: Int](networkchannel/maximumdatagramsize.md)
  Retrieve the maximum datagram size that can be sent on the channel. Any datagrams sent should be less than or equal to this size.
- [var messages: AsyncThrowingStream<ApplicationProtocol.Message<ApplicationProtocol.ContentType>, any Error>](networkchannel/messages.md)
  Receive data from a connection as an async stream.
- [var parameters: NWParameters](networkchannel/parameters.md)
  The set of parameters with which the channel was created
- [var state: NetworkChannel<ApplicationProtocol>.State](networkchannel/state-swift.property.md)
  Access the current state of the connection
### Instance Methods
- [func close(code: NWProtocolWebSocket.CloseCode, reason: String?, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/close(code:reason:metadata:).md)
  Send a WebSocket close frame on a connection.
- [func dataTransferReport() async throws -> NWConnection.DataTransferReport](networkchannel/datatransferreport.md)
  Start a data transfer report on a connection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last). This method will start the connection if it isn’t already started.
- [func establishmentReport() async throws -> NWConnection.EstablishmentReport](networkchannel/establishmentreport.md)
  Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, this method will wait until the connection becomes ready and then deliver the report. This method will start the connection if it isn’t already started.
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](networkchannel/metadata(definition:).md)
  Access connection-wide protocol metadata on the connection. This allows access to state for protocols like TCP and TLS that have long-term state.
- [func ping<Content>(Content?, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/ping(_:metadata:).md)
  Send a ping frame on a connection.
- [func pong<Content>(Content?, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/pong(_:metadata:).md)
  Send a pong frame on a connection.
- [func receive() async throws -> ApplicationProtocol.Message<Data>](networkchannel/receive-3a115.md)
  Receive data from a connection.
- [func receive() async throws -> ApplicationProtocol.Message<Data>](networkchannel/receive-3atum.md)
  Receive data from a connection.
- [func receive<Sending, Receiving, CoderType>() async throws -> ApplicationProtocol.Message<Receiving>](networkchannel/receive-5p11z.md)
  Receive an object from a connection.
- [func receive() async throws -> ApplicationProtocol.Message<Data>](networkchannel/receive-86md7.md)
  Receive data from a connection.
- [func receive<T>() async throws -> ApplicationProtocol.Message<Data>](networkchannel/receive-8jbul.md)
  Receive data on a connection.
- [func receive<Value>(as: Value.Type) async throws -> ApplicationProtocol.Message<Value>](networkchannel/receive(as:).md)
  Receive data from a connection as a fixed width integer.
- [func receive(atLeast: Int, atMost: Int) async throws -> ApplicationProtocol.Message<Data>](networkchannel/receive(atleast:atmost:).md)
  Receive data from a connection
- [func receive(exactly: Int) async throws -> ApplicationProtocol.Message<Data>](networkchannel/receive(exactly:).md)
  Receive data from a connection.
- [func send<Value>(Value, endOfStream: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:endofstream:metadata:)-4f2l0.md)
  Send fixed width integer on a connection. This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.
- [func send<Content>(Content, endOfStream: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:endofstream:metadata:)-79bb6.md)
  Send data on a connection.
- [func send<T>(Data, lastMessage: Bool, metadata: NWProtocolFramer.Message?, other: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:lastmessage:metadata:other:).md)
  Send data on a connection.
- [func send<Content>(Content, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:metadata:)-3r1av.md)
  Send binary frame on a WebSocket connection.
- [func send<Content>(Content, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:metadata:)-42nkz.md)
  Send data on a UDP connection.
- [func send<Sending, Receiving, CoderType>(Sending, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:metadata:)-4rxt1.md)
  Send data on a connection.
- [func send(String, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:metadata:)-5ec48.md)
  Send a text frame on a WebSocket connection.
- [func send<Content>(Content, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata]) async throws](networkchannel/send(_:type:lastmessage:metadata:).md)
  Send data on a connection.
- [func sendIdempotent<Content>(Content, endOfStream: Bool, metadata: () -> [NWProtocolMetadata])](networkchannel/sendidempotent(_:endofstream:metadata:)-4bo5u.md)
  Send data idempotently on a connection.
- [func sendIdempotent<Value>(Value, endOfStream: Bool, metadata: () -> [NWProtocolMetadata])](networkchannel/sendidempotent(_:endofstream:metadata:)-6cko0.md)
  Send data idempotently on a connection.
- [func sendIdempotent(String, metadata: () -> [NWProtocolMetadata])](networkchannel/sendidempotent(_:metadata:)-37eiq.md)
  Send an idempotent text frame on a WebSocket connection.
- [func sendIdempotent<Content>(Content, metadata: () -> [NWProtocolMetadata])](networkchannel/sendidempotent(_:metadata:)-6tubc.md)
  Send an idempotent binary frame on a WebSocket connection.
- [func sendIdempotent<Content>(Content, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata])](networkchannel/sendidempotent(_:type:lastmessage:metadata:).md)
  Send idempotent data on a connection.
- [func startReceive(((Int, Int) async throws -> ApplicationProtocol.Message<Data>) async throws -> Void) async throws](networkchannel/startreceive(_:).md)
  Receive partial data from a connection.
- [func startSend(String, metadata: () -> [NWProtocolMetadata], handler: ((String, Bool) async throws -> Void) async throws -> Void) async throws](networkchannel/startsend(_:metadata:handler:)-15tt3.md)
  Send partial text on a connection.
- [func startSend<Content>(Content, metadata: () -> [NWProtocolMetadata], handler: ((Content, Bool) async throws -> Void) async throws -> Void) async throws](networkchannel/startsend(_:metadata:handler:)-5xhjv.md)
  Send partial binary data on a connection.
### Enumerations
- [NetworkChannel.State](networkchannel/state-swift.enum.md)

## Relationships

### Inherited By
- [NetworkConnection](networkconnection.md)
- [QUIC.Datagrams](quic/datagrams.md)
- [QUIC.Stream](quic/stream.md)
### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel)*