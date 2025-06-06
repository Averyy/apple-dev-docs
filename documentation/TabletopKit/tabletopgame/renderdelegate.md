# TabletopGame.RenderDelegate

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for the object that renders your entire game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol RenderDelegate : AnyObject
```

#### Overview

To provide a renderer, set the [`TabletopGame`](tabletopgame.md) object render delegate to an object that conforms to this protocol using the [`addRenderDelegate(_:)`](tabletopgame/addrenderdelegate(_:).md) method. Then implement the [`onUpdate(timeInterval:snapshot:visualState:)`](tabletopgame/renderdelegate/onupdate(timeinterval:snapshot:visualstate:).md) protocol method to render the current state of the game.

## Topics

### Rendering the game
- [func onUpdate(timeInterval: Double, snapshot: TableSnapshot, visualState: TableVisualState)](tabletopgame/renderdelegate/onupdate(timeinterval:snapshot:visualstate:).md)
- [func updateRootPose(Pose3D)](tabletopgame/renderdelegate/updaterootpose(_:).md)

## Relationships

### Inherited By
- [EntityRenderDelegate](entityrenderdelegate.md)

## See Also

- [func addRenderDelegate(some TabletopGame.RenderDelegate)](tabletopgame/addrenderdelegate(_:).md)
- [func removeRenderDelegate(some TabletopGame.RenderDelegate)](tabletopgame/removerenderdelegate(_:).md)
- [protocol EntityRenderDelegate](entityrenderdelegate.md)
  A protocol for the object that renders your entire game using RealityKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/renderdelegate)*