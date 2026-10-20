# send(_:to:dataMode:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Transmits data to one or more players connected to the match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func send(_ data: Data, to players: [GKPlayer], dataMode mode: GKMatch.SendDataMode) throws
```

```objc
- (BOOL) sendData:(NSData *) data toPlayers:(NSArray<GKPlayer *> *) players dataMode:(GKMatchSendDataMode) mode error:(NSError **) error;
```

## Mentions

- [Exchanging data between players in real-time games](../exchanging-data-between-players-in-real-time-games.md)

#### Discussion

The match queues the data and transmits it when the network becomes available.

## Parameters

- `data`: The bytes to send.
- `players`: The players who receive the data.
- `mode`: The mechanism used to send the data.

## See Also

### Sending data to other players
- [func chooseBestHostingPlayer(completionHandler: (GKPlayer?) -> Void)](./choosebesthostingplayer%28completionhandler%29.md)
  Determines the best player in the game to act as the server for a client-server topology.
- [func sendData(toAllPlayers: Data, with: GKMatch.SendDataMode) throws](./senddata%28toallplayers,with%29.md)
  Transmits data to all players connected to the match.
- [GKMatch.SendDataMode](./senddatamode.md)
  The mechanism used to transmit data to other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/send(_:to:datamode:))*