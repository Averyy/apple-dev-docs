# nw_quic_set_webtransport_enabled(_:_:)

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
func nw_quic_set_webtransport_enabled(_ options: nw_protocol_options_t, _ enable_web_transport: Bool)
```

#### Discussion

Set whether the QUIC connection should support WebTransport. When enabled, WebTransport-specific features such as RESET_STREAM_AT and other extensions will be available.

## Parameters

- `options`: An nw_protocol_options_t for a QUIC connection.
- `enable_web_transport`: True to enable WebTransport support, false to disable. Defaults to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_quic_set_webtransport_enabled(_:_:))*