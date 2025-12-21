# sec_protocol_metadata_get_negotiated_ciphersuite(_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func sec_protocol_metadata_get_negotiated_ciphersuite(_ metadata: sec_protocol_metadata_t) -> SSLCipherSuite
```

#### Return Value

A SSLCipherSuite.

#### Discussion

Get the negotiated TLS ciphersuite.

## Parameters

- `metadata`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_ciphersuite(_:))*