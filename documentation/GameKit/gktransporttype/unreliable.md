# GKTransportType.unreliable

**Framework**: GameKit  
**Kind**: case

The data is sent once and is not sent again if a transmission error occurs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case unreliable
```

#### Discussion

Use this for small packets of data that must arrive quickly to be useful to the recipient.

## See Also

- [GKTransportType.reliable](gktransporttype/reliable.md)
  The data is sent continuously until it is successfully received by the intended recipients or the connection times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gktransporttype/unreliable)*