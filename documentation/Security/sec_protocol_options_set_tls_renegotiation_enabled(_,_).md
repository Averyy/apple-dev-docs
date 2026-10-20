# sec_protocol_options_set_tls_renegotiation_enabled(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

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
func sec_protocol_options_set_tls_renegotiation_enabled(_ options: sec_protocol_options_t, _ renegotiation_enabled: Bool)
```

```c
void sec_protocol_options_set_tls_renegotiation_enabled(sec_protocol_options_t options, bool renegotiation_enabled);
```

#### Discussion

Enable or disable TLS (1.2 and prior) session renegotiation. This defaults to `true`.

## Parameters

- `options`: A `sec_protocol_options_t` instance.
- `renegotiation_enabled`: Flag to enable or disable TLS (1.2 and prior) session renegotiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_renegotiation_enabled(_:_:))*