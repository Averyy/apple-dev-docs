# update(deltaTime:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func update(deltaTime: Double)
```

## See Also

### Creating a tabletop game
- [init(tableSetup: TableSetup, version: Int)](./init%28tablesetup,version%29.md)
  Creates a tabletop game with the specified table configuration and version of rules.
- [var rootPose: Pose3D](./rootpose.md)
  Update the root pose for the current player
- [func withCurrentSnapshot((TableSnapshot) -> Void)](./withcurrentsnapshot%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/update(deltatime:))*