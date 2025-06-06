# chooseBestHostPlayer(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Determines the best player in the game to act as the server for a client-server match.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func chooseBestHostPlayer() async -> String?
```

#### Discussion

Calling this method causes GameKit to attempt to estimate which player has the best overall network connection using a variety of metrics such as bandwidth, latency, and network reliability. Typically, you call this method when your game implements a client-server model on top of the match’s peer-to-peer connection.

## Parameters

- `completionHandler`: The block receives the following parameter:

## See Also

- [var playerIDs: [String]?](gkmatch/playerids.md)
  The player identifiers for remote players in the match.
- [func send(Data, toPlayers: [String], with: GKMatch.SendDataMode) throws](gkmatch/send(_:toplayers:with:).md)
  Transmits data to a list of connected players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/choosebesthostplayer(completionhandler:))*