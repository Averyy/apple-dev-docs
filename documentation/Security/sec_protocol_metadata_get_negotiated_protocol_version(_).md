# sec_protocol_metadata_get_negotiated_protocol_version(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_metadata_get_negotiated_tls_protocol_version(_:))
- iPadOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_metadata_get_negotiated_tls_protocol_version(_:))
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: sec_protocol_metadata_get_negotiated_tls_protocol_version(_:))
- macOS 10.14+ - Deprecated in 10.15 (renamed: sec_protocol_metadata_get_negotiated_tls_protocol_version(_:))
- tvOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_metadata_get_negotiated_tls_protocol_version(_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: sec_protocol_metadata_get_negotiated_tls_protocol_version(_:))
- watchOS 5.0+ - Deprecated in 6.0 (renamed: sec_protocol_metadata_get_negotiated_tls_protocol_version(_:))

## Declaration

```swift
func sec_protocol_metadata_get_negotiated_protocol_version(_ metadata: sec_protocol_metadata_t) -> SSLProtocol
```

```c
SSLProtocol sec_protocol_metadata_get_negotiated_protocol_version(sec_protocol_metadata_t metadata);
```

## Return Value

A SSLProtocol enum of the TLS version.

## Discussion

Get the negotiated TLS version.

## Parameters

- `metadata`: A `sec_protocol_metadata_t` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_protocol_version(_:))*