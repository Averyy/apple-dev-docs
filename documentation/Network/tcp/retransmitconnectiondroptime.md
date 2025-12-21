# retransmitConnectionDropTime(_:)

**Framework**: Network  
**Kind**: method

Set the TCP retransmission attempt timeout.

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
func retransmitConnectionDropTime(_ timeout: UInt32) -> TCP
```

#### Discussion

A timeout for TCP retransmission attempts, in seconds (`TCP_RXT_CONNDROPTIME`).

## Parameters

- `timeout`: The retransmission attempt timeout, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/retransmitconnectiondroptime(_:))*