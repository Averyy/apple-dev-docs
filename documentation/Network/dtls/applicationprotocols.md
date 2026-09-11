# applicationProtocols(_:)

**Framework**: Network  
**Kind**: method

Set application protocols supported by clients of this protocol.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func applicationProtocols(_ protocols: [String]) -> DTLS
```

#### Discussion

Application layer protocol negotiation (ALPN) tokens describe the application protocol in use above DTLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/applicationprotocols(_:))*