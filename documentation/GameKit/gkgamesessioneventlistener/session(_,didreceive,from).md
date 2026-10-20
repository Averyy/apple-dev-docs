# session(_:didReceive:from:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Tells the listener the player received data from another player.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func session(_ session: GKGameSession, didReceive data: Data, from player: GKCloudPlayer)
```

```objc
- (void) session:(GKGameSession *) session didReceiveData:(NSData *) data fromPlayer:(GKCloudPlayer *) player;
```

#### Discussion

This event fires after the [`send(_:with:completionHandler:)`](../gkgamesession/send%28_,with,completionhandler%29.md) method has been called. All connected players except the calling player are notified.

## Parameters

- `session`: The game session the sending player is associated with.
- `data`: The data sent by the player.
- `player`: The player sending data to all other connected players in the game session.

## See Also

### Transferring Data
- [func session(GKGameSession, didReceiveMessage: String, with: Data, from: GKCloudPlayer)](./session%28_,didreceivemessage,with,from%29.md)
  Tells the listener a player has received a message from another player.
- [func session(GKGameSession, player: GKCloudPlayer, didSave: Data)](./session%28_,player,didsave%29.md)
  Tells the listener data was saved by a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:didreceive:from:))*