# rootPose

**Framework**: TabletopKit  
**Kind**: property

Update the root pose for the current player

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var rootPose: Pose3D { get set }
```

## See Also

- [init(tableSetup: TableSetup, version: Int)](tabletopgame/init(tablesetup:version:).md)
  Creates a tabletop game with the specified table configuration and version of rules.
- [func update(deltaTime: Double)](tabletopgame/update(deltatime:).md)
  Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.
- [func withCurrentSnapshot((TableSnapshot) -> Void)](tabletopgame/withcurrentsnapshot(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/rootpose)*