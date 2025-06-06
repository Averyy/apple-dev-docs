# SKWarpable

**Framework**: SpriteKit  
**Kind**: protocol

A protocol for objects that can be warped and animated by an [`SKWarpGeometry`](skwarpgeometry.md).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol SKWarpable : NSObjectProtocol
```

## Mentions

- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)
- [Warping SpriteKit Content By Using an Effect Node](warping-spritekit-content-by-using-an-effect-node.md)

## Topics

### Instance Properties
- [var subdivisionLevels: Int](skwarpable/subdivisionlevels.md)
  The maximum number of subdivision iterations used to generate the final vertices.
- [var warpGeometry: SKWarpGeometry?](skwarpable/warpgeometry.md)
  The warp geometry used to define the distortion.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SKEffectNode](skeffectnode.md)
- [SKScene](skscene.md)
- [SKSpriteNode](skspritenode.md)

## See Also

- [class SKWarpGeometry](skwarpgeometry.md)
  A definition for a deformation of nodes that conform to [`SKWarpable`](skwarpable.md).
- [class SKWarpGeometryGrid](skwarpgeometrygrid.md)
  A definition for a grid-based deformation of nodes that conform to [`SKWarpable`](skwarpable.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skwarpable)*