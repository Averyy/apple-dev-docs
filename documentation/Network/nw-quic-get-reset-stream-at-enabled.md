# nw_quic_get_reset_stream_at_enabled(_:)

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
func nw_quic_get_reset_stream_at_enabled(_ options: nw_protocol_options_t) -> Bool
```

#### Return Value

True if RESET_STREAM_AT support is enabled, false otherwise.

#### Discussion

Get whether the QUIC connection has RESET_STREAM_AT enabled.

## Parameters

- `options`: An nw_protocol_options_t for a QUIC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_quic_get_reset_stream_at_enabled(_:))*