# inboundStreams(prepending:_:)

**Framework**: Network  
**Kind**: method

Handle inbound streams and provide a closure on which callback handlers will be executed. When the `NetworkConnection<QUIC>` state moves to `ready`, the internal listener is registered with the system and can receive incoming streams on the multiplexing instance. `inboundStreams` should only be called once on a `NetworkConnection<QUIC>`, and multiple calls to run will throw an exception.

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
final func inboundStreams<NewApplicationProtocol>(@ProtocolStackBuilder<NewApplicationProtocol> prepending: @escaping (QUICStream) -> NewApplicationProtocol, _ handler: @escaping @isolated(any) (QUIC.Stream<NewApplicationProtocol>) async throws -> Void) async throws where NewApplicationProtocol : OneToOneProtocol
```

#### Discussion

If the `NetworkConnection<QUIC>` is not started at the time that `inboundStreams` is invoked, it will be started.

The passed protocols in the `prepending` ProtocolStackBuilder will be added on top of the inbound streams.

The closure inherits the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/inboundstreams(prepending:_:))*