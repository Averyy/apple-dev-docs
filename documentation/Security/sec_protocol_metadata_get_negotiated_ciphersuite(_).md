# sec_protocol_metadata_get_negotiated_ciphersuite(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))
- iPadOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))
- Mac Catalyst 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))
- macOS 10.14+ - Deprecated in 10.15 (renamed: sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))
- tvOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))
- watchOS 5.0+ - Deprecated in 6.0 (renamed: sec_protocol_metadata_get_negotiated_tls_ciphersuite(_:))

## Declaration

```swift
func sec_protocol_metadata_get_negotiated_ciphersuite(_ metadata: sec_protocol_metadata_t) -> SSLCipherSuite
```

```c
SSLCipherSuite sec_protocol_metadata_get_negotiated_ciphersuite(sec_protocol_metadata_t metadata);
```

#### Return Value

A SSLCipherSuite.

#### Discussion

Get the negotiated TLS ciphersuite.

## Parameters

- `metadata`: A `sec_protocol_metadata_t` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_ciphersuite(_:))*