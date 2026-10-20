# send(_:toPlayers:with:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Transmits data to a list of connected players.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`sendData(toAllPlayers:with:)`](./senddata%28toallplayers,with%29.md) method instead.

## Declaration

```swift
func send(_ data: Data, toPlayers playerIDs: [String], with mode: GKMatch.SendDataMode) throws
```

```objc
- (BOOL) sendData:(NSData *) data toPlayers:(NSArray<NSString *> *) playerIDs withDataMode:(GKMatchSendDataMode) mode error:(NSError **) error;
```

#### Discussion

The match queues the data and transmits it when the network becomes available.

## Parameters

- `data`: The bytes to send.
- `playerIDs`: The identifier strings for the list of players who should receive the data.
- `mode`: The mechanism used to send the data.

## See Also

### Deprecated Methods and Properties
- [func chooseBestHostPlayer(completionHandler: (String?) -> Void)](./choosebesthostplayer%28completionhandler%29.md)
  Determines the best player in the game to act as the server for a client-server match.
- [var playerIDs: [String]?](./playerids.md)
  The player identifiers for remote players in the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/send(_:toplayers:with:))*