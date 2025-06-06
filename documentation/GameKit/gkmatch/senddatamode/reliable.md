# GKMatch.SendDataMode.reliable

**Framework**: GameKit  
**Kind**: case

Sends data continuously until the recipients successfully receive it or the connection times out.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case reliable
```

## Mentions

- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)

#### Discussion

Use this mode when you need guaranteed delivery in the order it’s sent, and the speed isn’t critical.

## See Also

- [GKMatch.SendDataMode.unreliable](gkmatch/senddatamode/unreliable.md)
  Sends data once even if an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/senddatamode/reliable)*