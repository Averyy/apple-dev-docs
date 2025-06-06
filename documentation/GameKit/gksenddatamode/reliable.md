# GKSendDataMode.reliable

**Framework**: GameKit  
**Kind**: case

The data is sent continuously until it is successfully received by the intended recipients or the connection times out.

**Availability**:
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case reliable
```

#### Discussion

Reliable transmissions are delivered in the order they were sent. Use this when you need to guarantee delivery.

## See Also

- [GKSendDataMode.unreliable](gksenddatamode/unreliable.md)
  The data is sent once and is not sent again if a transmission error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksenddatamode/reliable)*