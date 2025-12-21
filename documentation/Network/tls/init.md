# init(_:)

**Framework**: Network  
**Kind**: init

Create a TLS protocol to use in a protocol stack.

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
init(@ProtocolStackBuilder<TCP> _ builder: () -> TCP)
```

## Parameters

- `builder`: The protocol stack below TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls/init(_:))*