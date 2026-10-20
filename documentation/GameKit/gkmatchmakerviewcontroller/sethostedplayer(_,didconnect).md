# setHostedPlayer(_:didConnect:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Updates the connection status of a player in a hosted game.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setHostedPlayer(_ player: GKPlayer, didConnect connected: Bool)
```

```objc
- (void) setHostedPlayer:(GKPlayer *) player didConnect:(BOOL) connected;
```

## Mentions

- [Finding players for custom server-based games](../finding-players-for-custom-server-based-games.md)

#### Discussion

When you connect or disconnect a player from your server in a hosted game, use this method to update the player’s status that appears in the matchmaker view controllers on other player’s devices. For example, invoke this method after you connect a player from the [`matchmakerViewController(_:hostedPlayerDidAccept:)`](../gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,hostedplayerdidaccept%29.md) delegate method.

## Parameters

- `player`: The player whose status changed.
- `connected`: A Boolean value that indicates whether the player connected or disconnected from the hosted match.

## See Also

### Hosting matches
- [var isHosted: Bool](./ishosted.md)
  A Boolean value that indicates whether the match is hosted or peer-to-peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/sethostedplayer(_:didconnect:))*