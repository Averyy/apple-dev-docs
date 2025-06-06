# EntityRenderDelegate

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for the object that renders your entire game using RealityKit.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol EntityRenderDelegate : TabletopGame.RenderDelegate
```

## Topics

### Getting the root entity
- [var root: Entity](entityrenderdelegate/root.md)
### Rendering the table
- [func updateRootPose(Pose3D)](entityrenderdelegate/updaterootpose(_:).md)

## Relationships

### Inherits From
- [TabletopGame.RenderDelegate](tabletopgame/renderdelegate.md)

## See Also

- [func addRenderDelegate(some TabletopGame.RenderDelegate)](tabletopgame/addrenderdelegate(_:).md)
- [func removeRenderDelegate(some TabletopGame.RenderDelegate)](tabletopgame/removerenderdelegate(_:).md)
- [TabletopGame.RenderDelegate](tabletopgame/renderdelegate.md)
  A protocol for the object that renders your entire game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/entityrenderdelegate)*