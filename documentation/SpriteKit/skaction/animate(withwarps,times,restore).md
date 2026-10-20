# animate(withWarps:times:restore:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action to distort a node through a sequence of [`SKWarpGeometry`](../skwarpgeometry.md) objects.

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
class func animate(withWarps warps: [SKWarpGeometry], times: [NSNumber], restore: Bool) -> SKAction?
```

```objc
+ (SKAction *) animateWithWarps:(NSArray<SKWarpGeometry *> *) warps times:(NSArray<NSNumber *> *) times restore:(BOOL) restore;
```

#### Return Value

A new action object.

#### Discussion

The [`numberOfColumns`](../skwarpgeometrygrid/numberofcolumns.md) and [`numberOfRows`](../skwarpgeometrygrid/numberofrows.md) in each geometry in the sequence should match.

## Parameters

- `warps`: The sequence of warps to apply to the node.
- `times`: The times at which each warp distortion in the sequence should complete.
- `restore`: A Boolean specifying whether to restore the original node’s warpGeometry from before the action.

## See Also

### Animate the Warping of a Node
- [class func animate(withWarps: [SKWarpGeometry], times: [NSNumber]) -> SKAction?](./animate%28withwarps,times%29.md)
  Creates an action to distort a node through a sequence of [`SKWarpGeometry`](../skwarpgeometry.md) objects.
- [class func warp(to: SKWarpGeometry, duration: TimeInterval) -> SKAction?](./warp%28to,duration%29.md)
  Creates an action to distort a node based using an [`SKWarpGeometry`](../skwarpgeometry.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/animate(withwarps:times:restore:))*