# certificateValidator(_:)

**Framework**: Network  
**Kind**: method

Set a closure to provide custom verification of the peer’s credentials during the DTLS handshake.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func certificateValidator(_ handler: @escaping @isolated(any) @Sendable (sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> DTLS
```

#### Discussion

This closure may be called multiple times for each connection. It should return `true` if the credentials should be trusted and the handshake should proceed, `false` otherwise.

> ⚠️ **Warning**: Most apps should not override the default system handling, as doing so can result in insecure network connections and major security vulnerabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/certificatevalidator(_:))*