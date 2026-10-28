# sec_protocol_options_append_tls_ciphersuite_group(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

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
func sec_protocol_options_append_tls_ciphersuite_group(_ options: sec_protocol_options_t, _ group: tls_ciphersuite_group_t)
```

```c
void sec_protocol_options_append_tls_ciphersuite_group(sec_protocol_options_t options, tls_ciphersuite_group_t group);
```

## Discussion

Append a TLS ciphersuite group to the set of enabled ciphersuites.

## Parameters

- `options`: A `sec_protocol_options_t` instance.
- `group`: A tls_ciphersuite_group_t value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_append_tls_ciphersuite_group(_:_:))*