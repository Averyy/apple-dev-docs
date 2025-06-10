# sec_protocol_metadata_copy_negotiated_protocol(_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func sec_protocol_metadata_copy_negotiated_protocol(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

#### Return Value

A NULL-terminated string carrying the negotiated protocol.

#### Discussion

```None
 Copy the application protocol negotiated, e.g., via the TLS ALPN extension.
 The caller is expected to `free` the output string when no longer needed.
```

## Parameters

- `metadata`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_negotiated_protocol(_:))*