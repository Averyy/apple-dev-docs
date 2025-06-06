# GKSendDataMode.unreliable

**Framework**: GameKit  
**Kind**: case

The data is sent once and is not sent again if a transmission error occurred.

**Availability**:
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case unreliable
```

#### Discussion

Data transmitted unreliably may be received out of order by recipients. Use this for small packets of data that must arrive quickly to be useful to the recipient.

## See Also

- [GKSendDataMode.reliable](gksenddatamode/reliable.md)
  The data is sent continuously until it is successfully received by the intended recipients or the connection times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksenddatamode/unreliable)*