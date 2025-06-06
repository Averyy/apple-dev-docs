# sec_protocol_options_set_challenge_block(_:_:_:)

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
func sec_protocol_options_set_challenge_block(_ options: sec_protocol_options_t, _ challenge_block: @escaping sec_protocol_challenge_t, _ challenge_queue: dispatch_queue_t)
```

#### Discussion

```None
  Set the challenge block.
```

```None
  A `sec_protocol_challenge_t` block.
```

```None
  A `dispatch_queue_t` on which the challenge block should be called.
```

## Parameters

- `options`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_challenge_block(_:_:_:))*