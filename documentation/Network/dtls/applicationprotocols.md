# applicationProtocols(_:)

**Framework**: Network  
**Kind**: method

Set application protocols supported by clients of this protocol.

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
func applicationProtocols(_ protocols: [String]) -> DTLS
```

#### Discussion

Application layer protocol negotiation (ALPN) tokens describe the application protocol in use above DTLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/applicationprotocols(_:))*