# GKMatch.SendDataMode

**Framework**: GameKit  
**Kind**: enum

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

## Topics

### Modes
- [GKMatch.SendDataMode.reliable](gkmatch/senddatamode/reliable.md)
  Sends data continuously until the recipients successfully receive it or the connection times out.
- [GKMatch.SendDataMode.unreliable](gkmatch/senddatamode/unreliable.md)
  Sends data once even if an error occurs.
### Initializers
- [init?(rawValue: Int)](gkmatch/senddatamode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func chooseBestHostingPlayer(completionHandler: (GKPlayer?) -> Void)](gkmatch/choosebesthostingplayer(completionhandler:).md)
  Determines the best player in the game to act as the server for a client-server topology.
- [func send(Data, to: [GKPlayer], dataMode: GKMatch.SendDataMode) throws](gkmatch/send(_:to:datamode:).md)
  Transmits data to one or more players connected to the match.
- [func sendData(toAllPlayers: Data, with: GKMatch.SendDataMode) throws](gkmatch/senddata(toallplayers:with:).md)
  Transmits data to all players connected to the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/senddatamode)*