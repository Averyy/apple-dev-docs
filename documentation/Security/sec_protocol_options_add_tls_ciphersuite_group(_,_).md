# sec_protocol_options_add_tls_ciphersuite_group(_:_:)

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

> **Deprecated**: Use sec_protocol_options_append_tls_ciphersuite_group

## Declaration

```swift
func sec_protocol_options_add_tls_ciphersuite_group(_ options: sec_protocol_options_t, _ group: SSLCiphersuiteGroup)
```

```c
void sec_protocol_options_add_tls_ciphersuite_group(sec_protocol_options_t options, SSLCiphersuiteGroup group);
```

#### Discussion

Add a TLS ciphersuite group to the set of enabled ciphersuites.

## Parameters

- `options`: A `sec_protocol_options_t` instance.
- `group`: A SSLCipherSuiteGroup value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_add_tls_ciphersuite_group(_:_:))*