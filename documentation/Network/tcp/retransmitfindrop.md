# retransmitFinDrop(_:)

**Framework**: Network  
**Kind**: method

Configure TCP to drop the connection after a FIN does not receive an ACK.

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
func retransmitFinDrop(_ drop: Bool) -> TCP
```

#### Discussion

A boolean to cause TCP to drop its connection after not receiving an ACK after a FIN (`TCP_RXT_FINDROP`).

## Parameters

- `drop`: True to drop, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/retransmitfindrop(_:))*