# sendIdempotent(_:endOfStream:metadata:)

**Framework**: Network  
**Kind**: method

Send data idempotently on a connection.

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
func sendIdempotent<Content>(_ content: Content, endOfStream: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) where Content : DataProtocol
```

#### Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

Idempotent content may be sent multiple times when opening up a 0-RTT connection, so there is no completion block

## Parameters

- `content`: The bytes to send on the connection.
- `endOfStream`: Write-close this stream.
- `builder`: A builder for specifying metadata about the content to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/sendidempotent(_:endofstream:metadata:)-4bo5u)*