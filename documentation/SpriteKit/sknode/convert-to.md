# convert(_:to:)

**Framework**: SpriteKit  
**Kind**: method

Converts a point in this node’s coordinate system to the coordinate system of another node in the node tree.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func convert(_ point: CGPoint, to node: SKNode) -> CGPoint
```

## Mentions

- [Connecting Bodies with Joints](connecting-bodies-with-joints.md)
- [Converting Coordinate Spaces](converting-coordinate-spaces.md)

#### Return Value

The same point converted to the other node’s coordinate system.

## Parameters

- `point`: A point in this node’s coordinate system.
- `node`: Another node in the same node tree as this node.

## See Also

- [Converting Coordinate Spaces](converting-coordinate-spaces.md)
  Convert positions across the various coordinate spaces in a scene.
- [func convert(CGPoint, from: SKNode) -> CGPoint](sknode/convert(_:from:).md)
  Converts a point from the coordinate system of another node in the node tree to the coordinate system of this node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/convert(_:to:))*