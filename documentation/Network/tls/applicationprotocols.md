# applicationProtocols(_:)

**Framework**: Network  
**Kind**: method

Set application protocols supported by clients of this protocol.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func applicationProtocols(_ protocols: [String]) -> TLS
```

#### Discussion

Application layer protocol negotiation (ALPN) tokens describe the application protocol in use above TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls/applicationprotocols(_:))*