# earlyDataEnabled(_:)

**Framework**: Network  
**Kind**: method

Enable early data (0-RTT) for DTLS.

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
func earlyDataEnabled(_ enabled: Bool) -> DTLS
```

#### Discussion

> ⚠️ **Warning**: This may have security implications for application data. In particular, DTLS early data is replayable by a network attacker. You must account for this when sending data before the handshake is confirmed. See RFC 8446 for more information. You MUST NOT enable fast open without a specific application profile that defines its use.

## Parameters

- `enabled`: True to enable early data, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/earlydataenabled(_:))*