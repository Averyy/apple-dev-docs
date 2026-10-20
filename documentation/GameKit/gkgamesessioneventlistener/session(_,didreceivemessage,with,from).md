# session(_:didReceiveMessage:with:from:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Tells the listener a player has received a message from another player.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func session(_ session: GKGameSession, didReceiveMessage message: String, with data: Data, from player: GKCloudPlayer)
```

```objc
- (void) session:(GKGameSession *) session didReceiveMessage:(NSString *) message withData:(NSData *) data fromPlayer:(GKCloudPlayer *) player;
```

#### Discussion

This event fires after the [`sendMessage(withLocalizedFormatKey:arguments:data:to:badgePlayers:completionHandler:)`](../gkgamesession/sendmessage%28withlocalizedformatkey,arguments,data,to,badgeplayers,completionhandler%29.md) method has been called. Only players contained in the `players` argument of the [`sendMessage(withLocalizedFormatKey:arguments:data:to:badgePlayers:completionHandler:)`](../gkgamesession/sendmessage%28withlocalizedformatkey,arguments,data,to,badgeplayers,completionhandler%29.md) method are notified.

## Parameters

- `session`: The game session the sending player is associated with.
- `message`: A `String` containing the message sent to other players.
- `data`: Any data associated with the message. The value of this parameter can be `nil`.
- `player`: The player who sent the message.

## See Also

### Transferring Data
- [func session(GKGameSession, didReceive: Data, from: GKCloudPlayer)](./session%28_,didreceive,from%29.md)
  Tells the listener the player received data from another player.
- [func session(GKGameSession, player: GKCloudPlayer, didSave: Data)](./session%28_,player,didsave%29.md)
  Tells the listener data was saved by a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:didreceivemessage:with:from:))*