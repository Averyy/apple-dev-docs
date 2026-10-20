# EntityRenderDelegate

**Framework**: TabletopKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for the object that renders your entire game using RealityKit.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol EntityRenderDelegate : TabletopGame.RenderDelegate
```

## Topics

### Getting the root entity
- [var root: Entity](./entityrenderdelegate/root.md)
### Rendering the table
- [func updateRootPose(Pose3D)](./entityrenderdelegate/updaterootpose%28_%29.md)

## Relationships

### Inherits From
- [TabletopGame.RenderDelegate](./tabletopgame/renderdelegate.md)

## See Also

### Rendering the table
- [func addRenderDelegate(some TabletopGame.RenderDelegate)](./tabletopgame/addrenderdelegate%28_%29.md)
- [func removeRenderDelegate(some TabletopGame.RenderDelegate)](./tabletopgame/removerenderdelegate%28_%29.md)
- [TabletopGame.RenderDelegate](./tabletopgame/renderdelegate.md)
  A protocol for the object that renders your entire game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/entityrenderdelegate)*