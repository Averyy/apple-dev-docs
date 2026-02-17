# nw_quic_set_reset_stream_at_enabled(_:_:)

**Framework**: Network  
**Kind**: func

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
func nw_quic_set_reset_stream_at_enabled(_ options: nw_protocol_options_t, _ enable_reset_stream_at: Bool)
```

#### Discussion

Set whether the QUIC connection should support RESET_STREAM_AT. When enabled, the reset_stream_at transport parameter will be advertised during the QUIC handshake to indicate support for WebTransport features including partial reliable stream resets.

## Parameters

- `options`: An nw_protocol_options_t for a QUIC connection.
- `enable_reset_stream_at`: True to enable RESET_STREAM_AT support, false to disable. Defaults to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_quic_set_reset_stream_at_enabled(_:_:))*