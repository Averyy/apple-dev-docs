# session(_:player:didSave:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Tells the listener data was saved by a player.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func session(_ session: GKGameSession, player: GKCloudPlayer, didSave data: Data)
```

```objc
- (void) session:(GKGameSession *) session player:(GKCloudPlayer *) player didSaveData:(NSData *) data;
```

## Parameters

- `session`: The game session data was saved to.
- `player`: The player that just saved data.
- `data`: The data that was saved.

## See Also

### Transferring Data
- [func session(GKGameSession, didReceive: Data, from: GKCloudPlayer)](./session%28_,didreceive,from%29.md)
  Tells the listener the player received data from another player.
- [func session(GKGameSession, didReceiveMessage: String, with: Data, from: GKCloudPlayer)](./session%28_,didreceivemessage,with,from%29.md)
  Tells the listener a player has received a message from another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:player:didsave:))*