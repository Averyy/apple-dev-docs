# distance(_:to:in:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a constraint that keeps a node within a certain distance of a point in another node’s coordinate system.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func distance(_ range: SKRange, to point: CGPoint, in node: SKNode) -> Self
```

```objc
+ (instancetype) distance:(SKRange *) range toPoint:(CGPoint) point inNode:(SKNode *) node;
```

#### Return Value

A new constraint.

#### Discussion

Each time when constraints are applied, a line is projected between the node’s position and the target point. The distance between the two points is calculated, and if it lies outside the specified range, the node is pushed or pulled along this line until it lies within the range.

## Parameters

- `range`: The range of allowed distances.
- `point`: The point to use as the target point.
- `node`: The node whose coordinate system the point is specified in.

## See Also

### Creating Distance Constraints
- [class func distance(SKRange, to: SKNode) -> Self](./distance%28_,to%29-6507j.md)
  Creates a constraint that keeps a node within a certain distance of another node.
- [class func distance(SKRange, to: CGPoint) -> Self](./distance%28_,to%29-7yk7n.md)
  Creates a constraint that keeps a node within a certain distance of a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint/distance(_:to:in:))*