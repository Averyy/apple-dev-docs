# sec_protocol_metadata_get_negotiated_protocol(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_negotiated_protocol(_:))
- iPadOS 12.0+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_negotiated_protocol(_:))
- Mac Catalyst 13.1+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_negotiated_protocol(_:))
- macOS 10.14+ - Deprecated in 15.5 (renamed: sec_protocol_metadata_copy_negotiated_protocol(_:))
- tvOS 12.0+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_negotiated_protocol(_:))
- visionOS 1.0+ - Deprecated in 2.5 (renamed: sec_protocol_metadata_copy_negotiated_protocol(_:))
- watchOS 5.0+ - Deprecated in 11.5 (renamed: sec_protocol_metadata_copy_negotiated_protocol(_:))

## Declaration

```swift
func sec_protocol_metadata_get_negotiated_protocol(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

```c
const char *sec_protocol_metadata_get_negotiated_protocol(sec_protocol_metadata_t metadata);
```

#### Return Value

A NULL-terminated string carrying the negotiated protocol.

#### Discussion

Get the application protocol negotiated, e.g., via the TLS ALPN extension.

## Parameters

- `metadata`: A `sec_protocol_metadata_t` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_protocol(_:))*