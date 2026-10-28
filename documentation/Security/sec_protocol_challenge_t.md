# sec_protocol_challenge_t

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

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
typealias sec_protocol_challenge_t = (sec_protocol_metadata_t, @escaping sec_protocol_challenge_complete_t) -> Void
```

```c
typedef void (^)(NSObject<OS_sec_protocol_metadata> *, void (^)(NSObject<OS_sec_identity> *)) sec_protocol_challenge_t;
```

## Discussion

Block to be invoked when the protocol instance is issued a challenge (e.g., a TLS certificate request).

## Parameters

- `metadata`: A `sec_protocol_metadata_t` instance.
- `complete`: A `sec_protocol_challenge_complete_t` to be invoked when the challenge is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_challenge_t)*