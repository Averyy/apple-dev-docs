# animate(withWarps:times:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action to distort a node through a sequence of [`SKWarpGeometry`](skwarpgeometry.md) objects.

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
class func animate(withWarps warps: [SKWarpGeometry], times: [NSNumber]) -> SKAction?
```

## Mentions

- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)

#### Return Value

A new action object.

#### Discussion

The [`numberOfColumns`](skwarpgeometrygrid/numberofcolumns.md) and [`numberOfRows`](skwarpgeometrygrid/numberofrows.md) in each geometry in the sequence should match.

## Parameters

- `warps`: The sequence of warps to apply to the node.
- `times`: The times at which each warp distortion in the sequence should complete.

## See Also

- [class func animate(withWarps: [SKWarpGeometry], times: [NSNumber], restore: Bool) -> SKAction?](skaction/animate(withwarps:times:restore:).md)
  Creates an action to distort a node through a sequence of [`SKWarpGeometry`](skwarpgeometry.md) objects.
- [class func warp(to: SKWarpGeometry, duration: TimeInterval) -> SKAction?](skaction/warp(to:duration:).md)
  Creates an action to distort a node based using an [`SKWarpGeometry`](skwarpgeometry.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/animate(withwarps:times:))*