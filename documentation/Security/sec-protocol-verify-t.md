# sec_protocol_verify_t

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
typealias sec_protocol_verify_t = (sec_protocol_metadata_t, sec_trust_t, @escaping sec_protocol_verify_complete_t) -> Void
```

#### Discussion

```None
  Block to be invoked when the protocol instance must verify the peer.

  NOTE: this may be called one or more times for a given connection.
```

## Parameters

- `metadata`: A   instance.
- `trust_ref`: A   instance.
- `complete`: A   to be invoked when verification is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_verify_t)*