# init(tableSetup:version:)

**Framework**: TabletopKit  
**Kind**: init

Creates a tabletop game with the specified table configuration and version of rules.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
init(tableSetup: TableSetup, version: Int = 0)
```

#### Discussion

Players can only join multiplayer games when their rules version matches other players.

## Parameters

- `tableSetup`: The initial arrangement of seats, equipment,   and counters during gameplay.
- `version`: The version of rules for this game.

## See Also

- [var rootPose: Pose3D](tabletopgame/rootpose.md)
  Update the root pose for the current player
- [func update(deltaTime: Double)](tabletopgame/update(deltatime:).md)
  Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.
- [func withCurrentSnapshot((TableSnapshot) -> Void)](tabletopgame/withcurrentsnapshot(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/init(tablesetup:version:))*