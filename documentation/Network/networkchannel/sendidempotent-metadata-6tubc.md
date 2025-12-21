# sendIdempotent(_:metadata:)

**Framework**: Network  
**Kind**: method

Send an idempotent binary frame on a WebSocket connection.

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
func sendIdempotent<Content>(_ content: Content, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) where Content : DataProtocol
```

#### Discussion

Idempotent content is allowed to be sent before the connection is ready, and may be replayed across parallel connection attempts. This content can be sent as part of fast-open protocols, which allows the data to be sent out sooner than if it were required to wait for connection establishment.

> ⚠️ **Warning**: Idempotent content will be replayed multiple times on the network. It may be subject to weaker security protections than non-idempotent content.

Content that needs to be sensitive to sending backpressure should not be considered idempotent.

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

## Parameters

- `content`: Idempotent binary data to send.
- `builder`: A builder for specifying metadata about the content to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/sendidempotent(_:metadata:)-6tubc)*