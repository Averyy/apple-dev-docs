# GKMatch.SendDataMode.unreliable

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

Sends data once even if an error occurs.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case unreliable
```

```c
GKMatchSendDataUnreliable
```

## Mentions

- [Exchanging data between players in real-time games](../../exchanging-data-between-players-in-real-time-games.md)

## Discussion

Use this mode for small packets of data that must arrive quickly to be useful to the recipient. Unreliable data may arrive in a different order than when you sent it.

## See Also

### Modes
- [GKMatch.SendDataMode.reliable](./reliable.md)
  Sends data continuously until the recipients successfully receive it or the connection times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/senddatamode/unreliable)*