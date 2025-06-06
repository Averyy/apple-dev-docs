# distance(_:to:)

**Framework**: SpriteKit  
**Kind**: method

Creates a constraint that keeps a node within a certain distance of a point.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func distance(_ range: SKRange, to point: CGPoint) -> Self
```

#### Return Value

A new constraint.

#### Discussion

Each time when constraints are applied, a line is projected between the node’s position and the target point. The distance between the two points is calculated, and if it lies outside the specified range, the node is pushed or pulled along this line until it lies within the range.

## Parameters

- `range`: The range of allowed distances between the node and the point.
- `point`: A point in the coordinate system of the node’s parent that is used to calculate the distance.

## See Also

- [class func distance(SKRange, to: SKNode) -> Self](skconstraint/distance(_:to:)-6507j.md)
  Creates a constraint that keeps a node within a certain distance of another node.
- [class func distance(SKRange, to: CGPoint, in: SKNode) -> Self](skconstraint/distance(_:to:in:).md)
  Creates a constraint that keeps a node within a certain distance of a point in another node’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint/distance(_:to:)-7yk7n)*