# removePlayer(_:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Removes a player from the session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func removePlayer(_ player: AVPlayer)
```

```objc
- (void) removePlayer:(AVPlayer *) player;
```

## Parameters

- `player`: The player to remove from the session.

## See Also

### Managing players
- [var players: [AVPlayer]](./players.md)
  The array of players associated with the session.
- [func addPlayer(AVPlayer)](./addplayer%28_%29.md)
  Adds a player to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/removeplayer(_:))*