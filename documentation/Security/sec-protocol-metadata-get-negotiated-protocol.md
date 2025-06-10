# sec_protocol_metadata_get_negotiated_protocol(_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func sec_protocol_metadata_get_negotiated_protocol(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

#### Return Value

A NULL-terminated string carrying the negotiated protocol.

#### Discussion

```None
 Get the application protocol negotiated, e.g., via the TLS ALPN extension.
```

## Parameters

- `metadata`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_protocol(_:))*