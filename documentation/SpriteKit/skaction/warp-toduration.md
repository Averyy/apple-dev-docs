# warp(to:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action to distort a node based using an [`SKWarpGeometry`](skwarpgeometry.md) object.

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
class func warp(to warp: SKWarpGeometry, duration: TimeInterval) -> SKAction?
```

## Mentions

- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)

#### Return Value

A new action object.

#### Discussion

The [`numberOfColumns`](skwarpgeometrygrid/numberofcolumns.md) and [`numberOfRows`](skwarpgeometrygrid/numberofrows.md) in the node’s current geometry should match those of the specified geometry.

## Parameters

- `warp`: The warp geometry to distort the node to.
- `duration`: The duration of the animation.

## See Also

- [class func animate(withWarps: [SKWarpGeometry], times: [NSNumber]) -> SKAction?](skaction/animate(withwarps:times:).md)
  Creates an action to distort a node through a sequence of [`SKWarpGeometry`](skwarpgeometry.md) objects.
- [class func animate(withWarps: [SKWarpGeometry], times: [NSNumber], restore: Bool) -> SKAction?](skaction/animate(withwarps:times:restore:).md)
  Creates an action to distort a node through a sequence of [`SKWarpGeometry`](skwarpgeometry.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/warp(to:duration:))*