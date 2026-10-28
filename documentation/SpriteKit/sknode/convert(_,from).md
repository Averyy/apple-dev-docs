# convert(_:from:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Converts a point from the coordinate system of another node in the node tree to the coordinate system of this node.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func convert(_ point: CGPoint, from node: SKNode) -> CGPoint
```

```objc
- (CGPoint) convertPoint:(CGPoint) point fromNode:(SKNode *) node;
```

## Return Value

The same point converted to this node’s coordinate system.

## Parameters

- `point`: A point in the other node’s coordinate system.
- `node`: Another node in the same node tree as this node.

## See Also

### Converting Between Coordinate Systems of Different Nodes
- [Converting Coordinate Spaces](../converting-coordinate-spaces.md)
  Convert positions across the various coordinate spaces in a scene.
- [func convert(CGPoint, to: SKNode) -> CGPoint](./convert%28_,to%29.md)
  Converts a point in this node’s coordinate system to the coordinate system of another node in the node tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/convert(_:from:))*