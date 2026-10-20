# GKSendDataMode.unreliable

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The data is sent once and is not sent again if a transmission error occurred.

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
case unreliable
```

```c
GKSendDataUnreliable
```

#### Discussion

Data transmitted unreliably may be received out of order by recipients. Use this for small packets of data that must arrive quickly to be useful to the recipient.

## See Also

### Constants
- [GKSendDataMode.reliable](./reliable.md)
  The data is sent continuously until it is successfully received by the intended recipients or the connection times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksenddatamode/unreliable)*