# sec_protocol_options_set_pre_shared_key_selection_block(_:_:_:)

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
func sec_protocol_options_set_pre_shared_key_selection_block(_ options: sec_protocol_options_t, _ psk_selection_block: @escaping sec_protocol_pre_shared_key_selection_t, _ psk_selection_queue: dispatch_queue_t)
```

#### Discussion

Set the PSK selection block.

```None
 A `dispatch_queue_t` on which the PSK selection block should be called.
```

## Parameters

- `options`: A   instance.
- `psk_selection_block`: A   block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_pre_shared_key_selection_block(_:_:_:))*