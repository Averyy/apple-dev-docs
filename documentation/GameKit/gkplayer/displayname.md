# displayName

**Framework**: GameKit  
**Kind**: property

A string to display for the player.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var displayName: String { get }
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

The display name for a player depends on whether the player is a friend of the local player on the device. If the player is a friend of the local player, the display name is the actual name of the player. If the player isn’t a friend, the display name is the player’s alias.

## See Also

- [var alias: String](gkplayer/alias.md)
  A string the player chooses to identify themself to other players.
- [var isInvitable: Bool](gkplayer/isinvitable.md)
  A Boolean value that indicates whether the local player can send an invitation to the player.
- [var isFriend: Bool](gkplayer/isfriend.md)
  A Boolean value that indicates whether the player is a friend of the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/displayname)*