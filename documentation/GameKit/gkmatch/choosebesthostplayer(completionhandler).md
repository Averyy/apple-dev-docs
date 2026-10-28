# chooseBestHostPlayer(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Determines the best player in the game to act as the server for a client-server match.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`chooseBestHostingPlayer(completionHandler:)`](./choosebesthostingplayer%28completionhandler%29.md) method instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
func chooseBestHostPlayer(completionHandler: @escaping @Sendable (String?) -> Void)
```

*Mac Catalyst, visionOS*

```swift
func chooseBestHostPlayer() async -> String?
```

```objc
- (void) chooseBestHostPlayerWithCompletionHandler:(void (^)(NSString *playerID)) completionHandler;
```

## Discussion

Calling this method causes GameKit to attempt to estimate which player has the best overall network connection using a variety of metrics such as bandwidth, latency, and network reliability. Typically, you call this method when your game implements a client-server model on top of the match’s peer-to-peer connection.

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameter:

  - **`playerID`**: The player identifier for the player with the best estimated network performance, or `nil` if GameKit couldn’t find a best host player.

## See Also

### Deprecated Methods and Properties
- [var playerIDs: [String]?](./playerids.md)
  The player identifiers for remote players in the match.
- [func send(Data, toPlayers: [String], with: GKMatch.SendDataMode) throws](./send%28_,toplayers,with%29.md)
  Transmits data to a list of connected players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/choosebesthostplayer(completionhandler:))*