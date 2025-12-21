# fastOpenAllowed(_:)

**Framework**: Network  
**Kind**: method

Configure TCP to enable TCP Fast Open (TFO).

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
func fastOpenAllowed(_ allowed: Bool) -> TCP
```

#### Discussion

This may take effect even when TCP is not the top-level protocol in the protocol stack. For example, if TLS is running over TCP, the Client Hello message may be sent as fast open data.

If TCP is the top-level protocol in the stack (the one the application directly interacts with), TFO will be disabled unless the application indicated that it will provide its own fast open data by calling NWParameters.allowFastOpen.

## Parameters

- `allowed`: True to allow TFO, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/fastopenallowed(_:))*