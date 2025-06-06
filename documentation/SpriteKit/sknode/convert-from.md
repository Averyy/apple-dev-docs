# convert(_:from:)

**Framework**: SpriteKit  
**Kind**: method

Converts a point from the coordinate system of another node in the node tree to the coordinate system of this node.

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
@MainActor
func convert(_ point: CGPoint, from node: SKNode) -> CGPoint
```

#### Return Value

The same point converted to this node’s coordinate system.

## Parameters

- `point`: A point in the other node’s coordinate system.
- `node`: Another node in the same node tree as this node.

## See Also

- [Converting Coordinate Spaces](converting-coordinate-spaces.md)
  Convert positions across the various coordinate spaces in a scene.
- [func convert(CGPoint, to: SKNode) -> CGPoint](sknode/convert(_:to:).md)
  Converts a point in this node’s coordinate system to the coordinate system of another node in the node tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/convert(_:from:))*