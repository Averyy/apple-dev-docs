# sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func sec_protocol_options_set_tls_diffie_hellman_parameters(_ options: sec_protocol_options_t, _ params: dispatch_data_t)
```

#### Discussion

Set the supported Diffie-Hellman parameters.

## Parameters

- `options`: A   instance.
- `params`: A dispatch_data_t containing legacy Diffie-Hellman parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_diffie_hellman_parameters(_:_:))*