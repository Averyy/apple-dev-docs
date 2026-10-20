# rootPose

**Framework**: TabletopKit  
**Kind**: property  
**Role**: Instance Property

Update the root pose for the current player

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var rootPose: Pose3D { get set }
```

## See Also

### Creating a tabletop game
- [init(tableSetup: TableSetup, version: Int)](./init%28tablesetup,version%29.md)
  Creates a tabletop game with the specified table configuration and version of rules.
- [func update(deltaTime: Double)](./update%28deltatime%29.md)
  Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.
- [func withCurrentSnapshot((TableSnapshot) -> Void)](./withcurrentsnapshot%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/rootpose)*