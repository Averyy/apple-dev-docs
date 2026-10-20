# NetworkChannel

**Framework**: Network  
**Kind**: class  
**Role**: Class

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
- [static func == (NetworkChannel<ApplicationProtocol>, NetworkChannel<ApplicationProtocol>) -> Bool](./networkchannel/eqeq%28_,_%29.md)
  Compare two instances of NetworkChannel for equality
### Instance Properties
- [var debugDescription: String](./networkchannel/debugdescription.md)
  Generate a string representation of NetworkChannel suitable for logging
- [var id: String](./networkchannel/id.md)
  The stable identity of the entity associated with this instance.
- [var maximumDatagramSize: Int](./networkchannel/maximumdatagramsize.md)
  Retrieve the maximum datagram size that can be sent on the channel. Any datagrams sent should be less than or equal to this size.
- [var messages: AsyncThrowingStream<ApplicationProtocol.Message<ApplicationProtocol.ContentType>, any Error>](./networkchannel/messages.md)
  Receive data from a connection as an async stream.
- [var parameters: NWParameters](./networkchannel/parameters.md)
- [var state: NetworkChannel<ApplicationProtocol>.State](./networkchannel/state-swift.property.md)
  Access the current state of the connection
### Instance Methods
- [func close(code: NWProtocolWebSocket.CloseCode, reason: String?, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/close%28code,reason,metadata%29.md)
  Send a WebSocket close frame on a connection.
- [func dataTransferReport() async throws -> NWConnection.DataTransferReport](./networkchannel/datatransferreport%28%29.md)
  Start a data transfer report on a connection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last). This method will start the connection if it isn’t already started.
- [func establishmentReport() async throws -> NWConnection.EstablishmentReport](./networkchannel/establishmentreport%28%29.md)
  Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, this method will wait until the connection becomes ready and then deliver the report. This method will start the connection if it isn’t already started.
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](./networkchannel/metadata%28definition%29.md)
  Access connection-wide protocol metadata on the connection. This allows access to state for protocols like TCP and TLS that have long-term state.
- [func onBetterPathUpdate((Self, Bool) -> Void) -> Self](./networkchannel/onbetterpathupdate%28_%29.md)
  A better path being available indicates that the system thinks there is a preferred path or interface to use, compared to the one this connection is actively using. As an example, the connection is established over an expensive cellular interface and an unmetered Wi-Fi interface is now available.
- [func onPathUpdate((Self, NWPath) -> Void) -> Self](./networkchannel/onpathupdate%28_%29.md)
  Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled.
- [func onViabilityUpdate((Self, Bool) -> Void) -> Self](./networkchannel/onviabilityupdate%28_%29.md)
  Set a closure to be called when the connection’s viability changes, which may be called multiple times until the connection is cancelled.
- [func ping<Content>(Content?, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/ping%28_,metadata%29.md)
  Send a ping frame on a connection.
- [func pong<Content>(Content?, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/pong%28_,metadata%29.md)
  Send a pong frame on a connection.
- [func receive() async throws -> ApplicationProtocol.Message<Data>](./networkchannel/receive%28%29-3a115.md)
  Receive data from a connection.
- [func receive() async throws -> ApplicationProtocol.Message<Data>](./networkchannel/receive%28%29-3atum.md)
  Receive data from a connection.
- [func receive<Sending, Receiving, CoderType>() async throws -> ApplicationProtocol.Message<Receiving>](./networkchannel/receive%28%29-5p11z.md)
  Receive an object from a connection.
- [func receive() async throws -> ApplicationProtocol.Message<Data>](./networkchannel/receive%28%29-86md7.md)
  Receive data from a connection.
- [func receive<T>() async throws -> ApplicationProtocol.Message<Data>](./networkchannel/receive%28%29-8jbul.md)
  Receive data on a connection.
- [func receive<Value>(as: Value.Type) async throws -> ApplicationProtocol.Message<Value>](./networkchannel/receive%28as%29.md)
  Receive data from a connection as a fixed width integer.
- [func receive(atLeast: Int, atMost: Int) async throws -> ApplicationProtocol.Message<Data>](./networkchannel/receive%28atleast,atmost%29.md)
  Receive data from a connection
- [func receive(exactly: Int) async throws -> ApplicationProtocol.Message<Data>](./networkchannel/receive%28exactly%29.md)
  Receive data from a connection.
- [func send<Value>(Value, endOfStream: Bool, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,endofstream,metadata%29-4f2l0.md)
  Send fixed width integer on a connection. This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.
- [func send<Content>(Content, endOfStream: Bool, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,endofstream,metadata%29-79bb6.md)
  Send data on a connection.
- [func send<T>(Data, lastMessage: Bool, metadata: NWProtocolFramer.Message?, other: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,lastmessage,metadata,other%29.md)
  Send data on a connection.
- [func send<Content>(Content, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,metadata%29-3r1av.md)
  Send binary frame on a WebSocket connection.
- [func send<Content>(Content, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,metadata%29-42nkz.md)
  Send data on a UDP connection.
- [func send<Sending, Receiving, CoderType>(Sending, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,metadata%29-4rxt1.md)
  Send data on a connection.
- [func send(String, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,metadata%29-5ec48.md)
  Send a text frame on a WebSocket connection.
- [func send<Content>(Content, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata]) async throws](./networkchannel/send%28_,type,lastmessage,metadata%29.md)
  Send data on a connection.
- [func sendIdempotent<Content>(Content, endOfStream: Bool, metadata: () -> [NWProtocolMetadata])](./networkchannel/sendidempotent%28_,endofstream,metadata%29-4bo5u.md)
  Send data idempotently on a connection.
- [func sendIdempotent<Value>(Value, endOfStream: Bool, metadata: () -> [NWProtocolMetadata])](./networkchannel/sendidempotent%28_,endofstream,metadata%29-6cko0.md)
  Send data idempotently on a connection.
- [func sendIdempotent(String, metadata: () -> [NWProtocolMetadata])](./networkchannel/sendidempotent%28_,metadata%29-37eiq.md)
  Send an idempotent text frame on a WebSocket connection.
- [func sendIdempotent<Content>(Content, metadata: () -> [NWProtocolMetadata])](./networkchannel/sendidempotent%28_,metadata%29-6tubc.md)
  Send an idempotent binary frame on a WebSocket connection.
- [func sendIdempotent<Content>(Content, type: Int, lastMessage: Bool, metadata: () -> [NWProtocolMetadata])](./networkchannel/sendidempotent%28_,type,lastmessage,metadata%29.md)
  Send idempotent data on a connection.
- [func startReceive(((Int, Int) async throws -> ApplicationProtocol.Message<Data>) async throws -> Void) async throws](./networkchannel/startreceive%28_%29.md)
  Receive partial data from a connection.
- [func startSend(String, metadata: () -> [NWProtocolMetadata], handler: ((String, Bool) async throws -> Void) async throws -> Void) async throws](./networkchannel/startsend%28_,metadata,handler%29-15tt3.md)
  Send partial text on a connection.
- [func startSend<Content>(Content, metadata: () -> [NWProtocolMetadata], handler: ((Content, Bool) async throws -> Void) async throws -> Void) async throws](./networkchannel/startsend%28_,metadata,handler%29-5xhjv.md)
  Send partial binary data on a connection.
### Enumerations
- [NetworkChannel.State](./networkchannel/state-swift.enum.md)

## Relationships

### Inherited By
- [NetworkConnection](./networkconnection.md)
- [QUIC.Datagrams](./quic/datagrams.md)
- [QUIC.Stream](./quic/stream.md)
### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel)*