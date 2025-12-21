# send(_:endOfStream:metadata:)

**Framework**: Network  
**Kind**: method

Send fixed width integer on a connection. This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

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
func send<Value>(_ value: Value, endOfStream: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Value : NetworkFixedWidthInteger
```

## Parameters

- `value`: The integer to send on the connection
- `endOfStream`: Pass true to close the write side of the connection after enqueuing the data to send,   meaning that no more data can be sent
- `builder`: An optional builder for specifying metadata


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/send(_:endofstream:metadata:)-4f2l0)*