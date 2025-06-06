# withCurrentSnapshot(_:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func withCurrentSnapshot(_ callback: (TableSnapshot) -> Void)
```

## See Also

- [init(tableSetup: TableSetup, version: Int)](tabletopgame/init(tablesetup:version:).md)
  Creates a tabletop game with the specified table configuration and version of rules.
- [var rootPose: Pose3D](tabletopgame/rootpose.md)
  Update the root pose for the current player
- [func update(deltaTime: Double)](tabletopgame/update(deltatime:).md)
  Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/withcurrentsnapshot(_:))*