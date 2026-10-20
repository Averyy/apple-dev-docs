# init(alpn:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Create a QUIC protocol for use in a protocol stack.

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
init(alpn: [String])
```

#### Discussion

The application layer protocol negotiation (ALPN) tokens describe the application protocol in use above QUIC.

## Parameters

- `alpn`: An array of application layer protocol tokens to use for negotiation during the QUIC handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic/init(alpn:))*