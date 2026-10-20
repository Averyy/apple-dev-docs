# addPlayer(_:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Adds a player to the session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func addPlayer(_ player: AVPlayer)
```

```objc
- (void) addPlayer:(AVPlayer *) player;
```

## Parameters

- `player`: The player instance to add to the session.

## See Also

### Managing players
- [var players: [AVPlayer]](./players.md)
  The array of players associated with the session.
- [func removePlayer(AVPlayer)](./removeplayer%28_%29.md)
  Removes a player from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/addplayer(_:))*