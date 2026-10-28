# sendData(toAllPlayers:with:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Transmits data to all players connected to the match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func sendData(toAllPlayers data: Data, with mode: GKMatch.SendDataMode) throws
```

```objc
- (BOOL) sendDataToAllPlayers:(NSData *) data withDataMode:(GKMatchSendDataMode) mode error:(NSError **) error;
```

## Mentions

- [Exchanging data between players in real-time games](../exchanging-data-between-players-in-real-time-games.md)

## Discussion

The match queues the data and transmits it when the network becomes available.

## Parameters

- `data`: The bytes to send.
- `mode`: The mechanism used to send the data.

## See Also

### Sending data to other players
- [func chooseBestHostingPlayer(completionHandler: (GKPlayer?) -> Void)](./choosebesthostingplayer%28completionhandler%29.md)
  Determines the best player in the game to act as the server for a client-server topology.
- [func send(Data, to: [GKPlayer], dataMode: GKMatch.SendDataMode) throws](./send%28_,to,datamode%29.md)
  Transmits data to one or more players connected to the match.
- [GKMatch.SendDataMode](./senddatamode.md)
  The mechanism used to transmit data to other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/senddata(toallplayers:with:))*