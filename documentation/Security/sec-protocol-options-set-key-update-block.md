# sec_protocol_options_set_key_update_block(_:_:_:)

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
func sec_protocol_options_set_key_update_block(_ options: sec_protocol_options_t, _ key_update_block: @escaping sec_protocol_key_update_t, _ key_update_queue: dispatch_queue_t)
```

#### Discussion

```None
 Set the key update block.
```

```None
 A `dispatch_queue_t` on which the key update block should be called.
```

## Parameters

- `options`: A   instance.
- `key_update_block`: A   block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_key_update_block(_:_:_:))*