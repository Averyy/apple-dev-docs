# verifyBlock(_:)

**Framework**: Network  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func verifyBlock(_ handler: @escaping @isolated(any) (sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> TLS
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls/verifyblock(_:))*