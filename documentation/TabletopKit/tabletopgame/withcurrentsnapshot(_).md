# withCurrentSnapshot(_:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func withCurrentSnapshot(_ callback: (TableSnapshot) -> Void)
```

## See Also

### Creating a tabletop game
- [init(tableSetup: TableSetup, version: Int)](./init%28tablesetup,version%29.md)
  Creates a tabletop game with the specified table configuration and version of rules.
- [var rootPose: Pose3D](./rootpose.md)
  Update the root pose for the current player
- [func update(deltaTime: Double)](./update%28deltatime%29.md)
  Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/withcurrentsnapshot(_:))*