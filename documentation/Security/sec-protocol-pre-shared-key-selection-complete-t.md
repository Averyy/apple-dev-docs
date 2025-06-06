# sec_protocol_pre_shared_key_selection_complete_t

**Framework**: Security  
**Kind**: typealias

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias sec_protocol_pre_shared_key_selection_complete_t = (dispatch_data_t?) -> Void
```

#### Discussion

```None
  Block to be invoked when a PSK selection event is complete and a PSK identity is chosen.
```

## Parameters

- `psk_identity`: A   instance carrying the chosen PSK identity, or nil if one does not match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_pre_shared_key_selection_complete_t)*