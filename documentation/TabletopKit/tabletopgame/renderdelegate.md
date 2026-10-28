# TabletopGame.RenderDelegate

**Framework**: TabletopKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for the object that renders your entire game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol RenderDelegate : AnyObject
```

## Overview

To provide a renderer, set the [`TabletopGame`](../tabletopgame.md) object render delegate to an object that conforms to this protocol using the [`addRenderDelegate(_:)`](./addrenderdelegate%28_%29.md) method. Then implement the [`onUpdate(timeInterval:snapshot:visualState:)`](./renderdelegate/onupdate%28timeinterval,snapshot,visualstate%29.md) protocol method to render the current state of the game.

## Topics

### Rendering the game
- [func onUpdate(timeInterval: Double, snapshot: TableSnapshot, visualState: TableVisualState)](./renderdelegate/onupdate%28timeinterval,snapshot,visualstate%29.md)
- [func updateRootPose(Pose3D)](./renderdelegate/updaterootpose%28_%29.md)

## Relationships

### Inherited By
- [EntityRenderDelegate](../entityrenderdelegate.md)

## See Also

### Rendering the table
- [func addRenderDelegate(some TabletopGame.RenderDelegate)](./addrenderdelegate%28_%29.md)
- [func removeRenderDelegate(some TabletopGame.RenderDelegate)](./removerenderdelegate%28_%29.md)
- [protocol EntityRenderDelegate](../entityrenderdelegate.md)
  A protocol for the object that renders your entire game using RealityKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/renderdelegate)*