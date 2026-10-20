# GKPlayerIDNoLongerAvailable

**Framework**: GameKit  
**Kind**: var  
**Role**: Global Variable

A constant for a player ID that’s no longer available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let GKPlayerIDNoLongerAvailable: String
```

```c
extern NSString * const GKPlayerIDNoLongerAvailable;
```

#### Discussion

Deprecated methods that previously returned the player ID return this constant.

## See Also

### Identifying the player
- [var gamePlayerID: String](./gkplayer/gameplayerid.md)
  A unique identifier for a player of the game.
- [var teamPlayerID: String](./gkplayer/teamplayerid.md)
  A unique identifier for a player of all the games that you distribute using your developer account.
- [func scopedIDsArePersistent() -> Bool](./gkplayer/scopedidsarepersistent%28%29.md)
  Returns a Boolean value depending on whether the player identifiers are persistent across game instances or unique to the game instance.
- [var playerID: String](./gkplayer/playerid.md)
  A unique identifier for a player of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayeridnolongeravailable)*