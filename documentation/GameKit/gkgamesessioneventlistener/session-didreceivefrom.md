# session(_:didReceive:from:)

**Framework**: GameKit  
**Kind**: method

Tells the listener the player received data from another player.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func session(_ session: GKGameSession, didReceive data: Data, from player: GKCloudPlayer)
```

#### Discussion

This event fires after the [`send(_:with:completionHandler:)`](gkgamesession/send(_:with:completionhandler:).md) method has been called. All connected players except the calling player are notified.

## Parameters

- `session`: The game session the sending player is associated with.
- `data`: The data sent by the player.
- `player`: The player sending data to all other connected players in the game session.

## See Also

- [func session(GKGameSession, didReceiveMessage: String, with: Data, from: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didreceivemessage:with:from:).md)
  Tells the listener a player has received a message from another player.
- [func session(GKGameSession, player: GKCloudPlayer, didSave: Data)](gkgamesessioneventlistener/session(_:player:didsave:).md)
  Tells the listener data was saved by a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:didreceive:from:))*