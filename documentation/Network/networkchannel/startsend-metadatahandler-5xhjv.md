# startSend(_:metadata:handler:)

**Framework**: Network  
**Kind**: method

Send partial binary data on a connection.

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
func startSend<Content>(_ content: Content, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}, handler: ((Content, Bool) async throws -> Void) async throws -> Void) async throws where Content : DataProtocol
```

#### Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

## Parameters

- `content`: The binary data to send.
- `builder`: A builder for specifying metadata about the content to send.
- `handler`: A handler that will be invoked immediately, and will be passed a closure   that should be called repeatedly until all binary data is sent.   Intermediate invocations of the send closure must be invoked with    set to false. The last call to the send closure must be   invoked with   set to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/startsend(_:metadata:handler:)-5xhjv)*