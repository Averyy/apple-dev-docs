# init(_:)

**Framework**: Network  
**Kind**: init

Create a DTLS protocol to use in a protocol stack.

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
init(@ProtocolStackBuilder<UDP> _ builder: () -> UDP)
```

## Parameters

- `builder`: The protocol stack below DTLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/init(_:))*