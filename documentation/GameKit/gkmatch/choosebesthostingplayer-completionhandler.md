# chooseBestHostingPlayer(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Determines the best player in the game to act as the server for a client-server topology.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func chooseBestHostingPlayer() async -> GKPlayer?
```

## Mentions

- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)

#### Discussion

This method estimates which player has the best network connection using a variety of metrics such as bandwidth, latency, and network reliability. Use this method to choose the player that acts as the server when you implement a client-server topology on top of the match’s peer-to-peer connection.

## Parameters

- `completionHandler`: The block receives the following parameter:

## See Also

- [func send(Data, to: [GKPlayer], dataMode: GKMatch.SendDataMode) throws](gkmatch/send(_:to:datamode:).md)
  Transmits data to one or more players connected to the match.
- [func sendData(toAllPlayers: Data, with: GKMatch.SendDataMode) throws](gkmatch/senddata(toallplayers:with:).md)
  Transmits data to all players connected to the match.
- [GKMatch.SendDataMode](gkmatch/senddatamode.md)
  The mechanism used to transmit data to other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/choosebesthostingplayer(completionhandler:))*