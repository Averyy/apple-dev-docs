# sec_protocol_pre_shared_key_selection_t

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
typealias sec_protocol_pre_shared_key_selection_t = (sec_protocol_metadata_t, dispatch_data_t?, @escaping sec_protocol_pre_shared_key_selection_complete_t) -> Void
```

#### Discussion

```None
  Block to be invoked when the client must choose a PSK identity given a hint from its peer.
```

## Parameters

- `metadata`: A   instance.
- `psk_identity_hint`: A   object carrying the peer’s (optional) PSK identity hint.
- `complete`: A   block to be invoked when PSK selection is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_pre_shared_key_selection_t)*