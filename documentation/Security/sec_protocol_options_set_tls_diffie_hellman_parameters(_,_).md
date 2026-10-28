# sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.14+ - Deprecated in 10.15
- tvOS 12.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 6.0

> **Deprecated**: DHE ciphersuites are no longer supported

## Declaration

```swift
func sec_protocol_options_set_tls_diffie_hellman_parameters(_ options: sec_protocol_options_t, _ params: dispatch_data_t)
```

```c
void sec_protocol_options_set_tls_diffie_hellman_parameters(sec_protocol_options_t options, dispatch_data_t params);
```

## Discussion

Set the supported Diffie-Hellman parameters.

## Parameters

- `options`: A `sec_protocol_options_t` instance.
- `params`: A dispatch_data_t containing legacy Diffie-Hellman parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:))*