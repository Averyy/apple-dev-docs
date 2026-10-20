# GKSendDataMode.reliable

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The data is sent continuously until it is successfully received by the intended recipients or the connection times out.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: No longer supported

## Declaration

```swift
case reliable
```

```c
GKSendDataReliable
```

#### Discussion

Reliable transmissions are delivered in the order they were sent. Use this when you need to guarantee delivery.

## See Also

### Constants
- [GKSendDataMode.unreliable](./unreliable.md)
  The data is sent once and is not sent again if a transmission error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksenddatamode/reliable)*