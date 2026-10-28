# sec_protocol_options_add_tls_ciphersuite(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 12.0+ - Deprecated in 13.0
- macOS 10.14+ - Deprecated in 10.15
- tvOS 12.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 6.0

> **Deprecated**: Use sec_protocol_options_append_tls_ciphersuite

## Declaration

```swift
func sec_protocol_options_add_tls_ciphersuite(_ options: sec_protocol_options_t, _ ciphersuite: SSLCipherSuite)
```

```c
void sec_protocol_options_add_tls_ciphersuite(sec_protocol_options_t options, SSLCipherSuite ciphersuite);
```

## Discussion

Add a TLS ciphersuite to the set of enabled ciphersuites.

## Parameters

- `options`: A `sec_protocol_options_t` instance.
- `ciphersuite`: A SSLCipherSuite value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_add_tls_ciphersuite(_:_:))*