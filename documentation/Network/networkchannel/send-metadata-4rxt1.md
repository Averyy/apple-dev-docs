# send(_:metadata:)

**Framework**: Network  
**Kind**: method

Send data on a connection.

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
func send<Sending, Receiving, CoderType>(_ content: Sending, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where ApplicationProtocol == Coder<Sending, Receiving, CoderType>, Sending : Encodable, Receiving : Decodable, CoderType : NetworkCoder
```

#### Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

## Parameters

- `content`: Object to send. The object will be encoded and then sent.
- `builder`: A builder for specifying metadata about the content to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/send(_:metadata:)-4rxt1)*