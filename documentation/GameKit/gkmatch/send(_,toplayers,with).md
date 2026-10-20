# send(_:toPlayers:with:)

**Framework**: GameKit  
**Kind**: method

Transmits data to a list of connected players.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func send(_ data: Data, toPlayers playerIDs: [String], with mode: GKMatch.SendDataMode) throws
```

#### Discussion

The match queues the data and transmits it when the network becomes available.

## Parameters

- `data`: The bytes to send.
- `playerIDs`: The identifier strings for the list of players who should receive the data.
- `mode`: The mechanism used to send the data.

## See Also

- [func chooseBestHostPlayer(completionHandler: (String?) -> Void)](gkmatch/choosebesthostplayer(completionhandler:).md)
  Determines the best player in the game to act as the server for a client-server match.
- [var playerIDs: [String]?](gkmatch/playerids.md)
  The player identifiers for remote players in the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/send(_:toplayers:with:))*