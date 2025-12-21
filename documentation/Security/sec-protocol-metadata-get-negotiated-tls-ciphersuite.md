# sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func sec_protocol_metadata_get_negotiated_tls_ciphersuite(_ metadata: sec_protocol_metadata_t) -> tls_ciphersuite_t
```

#### Return Value

A `tls_ciphersuite_t`.

#### Discussion

Get the negotiated TLS ciphersuite.

## Parameters

- `metadata`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))*