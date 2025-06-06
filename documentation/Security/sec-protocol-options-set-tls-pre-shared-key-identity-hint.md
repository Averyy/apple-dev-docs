# sec_protocol_options_set_tls_pre_shared_key_identity_hint(_:_:)

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
func sec_protocol_options_set_tls_pre_shared_key_identity_hint(_ options: sec_protocol_options_t, _ psk_identity_hint: dispatch_data_t)
```

#### Discussion

```None
  Set the PSK identity hint to use by servers when negotiating a PSK ciphersuite.
  See https://tools.ietf.org/html/rfc4279 for more details.
```

## Parameters

- `options`: A   instance.
- `psk_identity_hint`: A dispatch_data_t containing a PSK identity hint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_pre_shared_key_identity_hint(_:_:))*