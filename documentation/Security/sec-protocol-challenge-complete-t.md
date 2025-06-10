# sec_protocol_challenge_complete_t

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
typealias sec_protocol_challenge_complete_t = (sec_identity_t?) -> Void
```

#### Discussion

```None
 Block to be invoked when an identity (authentication) challenge is complete.

 Note: prior to macOS 10.15, iOS 13.0, watchOS 6.0, and tvOS 13.0, calling this
 block with a NULL `identity` argument was prohibited.
```

## Parameters

- `identity`: A   containing the identity to use for this challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_challenge_complete_t)*