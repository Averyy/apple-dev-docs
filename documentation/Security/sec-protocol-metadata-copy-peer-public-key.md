# sec_protocol_metadata_copy_peer_public_key(_:)

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
func sec_protocol_metadata_copy_peer_public_key(_ metadata: sec_protocol_metadata_t) -> dispatch_data_t?
```

#### Return Value

A `dispatch_data_t` containing the peer’s raw public key.

#### Discussion

```None
 Get the protocol instance peer's public key.
```

## Parameters

- `metadata`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_peer_public_key(_:))*