# GKMatch.SendDataMode

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The mechanism used to transmit data to other players.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum SendDataMode
```

```c
enum GKMatchSendDataMode : NSInteger;
```

## Topics

### Modes
- [GKMatch.SendDataMode.reliable](./senddatamode/reliable.md)
  Sends data continuously until the recipients successfully receive it or the connection times out.
- [GKMatch.SendDataMode.unreliable](./senddatamode/unreliable.md)
  Sends data once even if an error occurs.
### Initializers
- [init?(rawValue: Int)](./senddatamode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending data to other players
- [func chooseBestHostingPlayer(completionHandler: (GKPlayer?) -> Void)](./choosebesthostingplayer%28completionhandler%29.md)
  Determines the best player in the game to act as the server for a client-server topology.
- [func send(Data, to: [GKPlayer], dataMode: GKMatch.SendDataMode) throws](./send%28_,to,datamode%29.md)
  Transmits data to one or more players connected to the match.
- [func sendData(toAllPlayers: Data, with: GKMatch.SendDataMode) throws](./senddata%28toallplayers,with%29.md)
  Transmits data to all players connected to the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/senddatamode)*