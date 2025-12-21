# send(_:metadata:)

**Framework**: Network  
**Kind**: method

Send binary frame on a WebSocket connection.

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
func send<Content>(_ content: Content, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Content : DataProtocol
```

#### Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

## Parameters

- `content`: Data to send.
- `builder`: A builder for specifying metadata about the content to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/send(_:metadata:)-3r1av)*