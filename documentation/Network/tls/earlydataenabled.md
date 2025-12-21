# earlyDataEnabled(_:)

**Framework**: Network  
**Kind**: method

Enable early data (0-RTT) for TLS.

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
func earlyDataEnabled(_ enabled: Bool) -> TLS
```

#### Discussion

> ⚠️ **Warning**: This may have security implications for application data. In particular, TLS early data is replayable by a network attacker. You must account for this when sending data before the handshake is confirmed. See RFC 8446 for more information. You MUST NOT enable fast open without a specific application profile that defines its use.

## Parameters

- `enabled`: True to enable early data, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls/earlydataenabled(_:))*