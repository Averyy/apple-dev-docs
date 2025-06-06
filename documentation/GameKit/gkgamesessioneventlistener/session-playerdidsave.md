# session(_:player:didSave:)

**Framework**: GameKit  
**Kind**: method

Tells the listener data was saved by a player.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func session(_ session: GKGameSession, player: GKCloudPlayer, didSave data: Data)
```

## Parameters

- `session`: The game session data was saved to.
- `player`: The player that just saved data.
- `data`: The data that was saved.

## See Also

- [func session(GKGameSession, didReceive: Data, from: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didreceive:from:).md)
  Tells the listener the player received data from another player.
- [func session(GKGameSession, didReceiveMessage: String, with: Data, from: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didreceivemessage:with:from:).md)
  Tells the listener a player has received a message from another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:player:didsave:))*