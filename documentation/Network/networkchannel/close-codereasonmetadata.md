# close(code:reason:metadata:)

**Framework**: Network  
**Kind**: method

Send a WebSocket close frame on a connection.

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
func close(code: NWProtocolWebSocket.CloseCode = .protocolCode(.normalClosure), reason: String? = nil, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws
```

#### Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

## Parameters

- `code`: Optional close code. Defaults to normal closure.
- `reason`: Optional reason string containing details about the closure.
- `builder`: A builder for specifying metadata about the content to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/close(code:reason:metadata:))*