# sec_protocol_options_add_pre_shared_key(_:_:_:)

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
func sec_protocol_options_add_pre_shared_key(_ options: sec_protocol_options_t, _ psk: dispatch_data_t, _ psk_identity: dispatch_data_t)
```

#### Discussion

```None
  Add a pre-shared key (PSK) and its identity to the options.
```

## Parameters

- `options`: A   instance.
- `psk`: A dispatch_data_t containing a PSK blob.
- `psk_identity`: A dispatch_data_t containing a PSK identity blob.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_add_pre_shared_key(_:_:_:))*