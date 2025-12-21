# ackStretchingDisabled(_:)

**Framework**: Network  
**Kind**: method

Disable ACK stretching.

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
func ackStretchingDisabled(_ disableAckStretching: Bool) -> TCP
```

#### Discussion

A boolean to cause TCP to disable ACK stretching (`TCP_SENDMOREACKS`).

## Parameters

- `disableAckStretching`: True to disable ACK stretching, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/ackstretchingdisabled(_:))*