# session(_:didReceiveMessage:with:from:)

**Framework**: GameKit  
**Kind**: method

Tells the listener a player has received a message from another player.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func session(_ session: GKGameSession, didReceiveMessage message: String, with data: Data, from player: GKCloudPlayer)
```

#### Discussion

This event fires after the [`sendMessage(withLocalizedFormatKey:arguments:data:to:badgePlayers:completionHandler:)`](gkgamesession/sendmessage(withlocalizedformatkey:arguments:data:to:badgeplayers:completionhandler:).md) method has been called. Only players contained in the `players` argument of the [`sendMessage(withLocalizedFormatKey:arguments:data:to:badgePlayers:completionHandler:)`](gkgamesession/sendmessage(withlocalizedformatkey:arguments:data:to:badgeplayers:completionhandler:).md) method are notified.

## Parameters

- `session`: The game session the sending player is associated with.
- `message`: A   containing the message sent to other players.
- `data`: Any data associated with the message. The value of this parameter can be  .
- `player`: The player who sent the message.

## See Also

- [func session(GKGameSession, didReceive: Data, from: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didreceive:from:).md)
  Tells the listener the player received data from another player.
- [func session(GKGameSession, player: GKCloudPlayer, didSave: Data)](gkgamesessioneventlistener/session(_:player:didsave:).md)
  Tells the listener data was saved by a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:didreceivemessage:with:from:))*