# update(deltaTime:)

**Framework**: TabletopKit  
**Kind**: method

Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func update(deltaTime: Double)
```

## See Also

- [init(tableSetup: TableSetup, version: Int)](tabletopgame/init(tablesetup:version:).md)
  Creates a tabletop game with the specified table configuration and version of rules.
- [var rootPose: Pose3D](tabletopgame/rootpose.md)
  Update the root pose for the current player
- [func withCurrentSnapshot((TableSnapshot) -> Void)](tabletopgame/withcurrentsnapshot(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/update(deltatime:))*