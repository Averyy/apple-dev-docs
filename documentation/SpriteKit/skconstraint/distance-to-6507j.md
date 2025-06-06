# distance(_:to:)

**Framework**: SpriteKit  
**Kind**: method

Creates a constraint that keeps a node within a certain distance of another node.

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
class func distance(_ range: SKRange, to node: SKNode) -> Self
```

#### Return Value

A new constraint.

#### Discussion

Distance constraints constrain a node to a specified distance range of another node or a point and can be used for effects such a simulating flocking around a node, repulsive fields and trails. Supplying a distance constraint with a range with a lower limit, an upper limit or both results in very different behaviors:

| Example initialization | Behavior |
| --- | --- |
| `SKConstraint.distance(SKRange(lowerLimit: 20), to: targetNode)` | If `targetNode` is moving and constrained objects are static, gives an effect similar to a repulsive magnetic field |
| `SKConstraint.distance(SKRange(upperLimit: 10), to: targetNode)` | All constrained nodes are immediately attracted to `targetNode`. Multiple constrained nodes can converge to a single point if `targetNode` is moved. |
| `SKConstraint.distance(SKRange(lowerLimit: 40, upperLimit: 50), to: targetNode)` | All constrained nodes are immediately attracted to `targetNode`. Multiple constrained nodes can form a ring around `targetNode` if it is moved. |

Each time when constraints are applied, a line is projected between the node’s position and the target node’s position. The distance between the two points is calculated, and if it lies outside the specified range, the node is pushed or pulled along this line until it lies within the range.

## Parameters

- `range`: The range of allowed distances between the two nodes.
- `node`: The target node used to calculate the distance.

## See Also

- [class func distance(SKRange, to: CGPoint) -> Self](skconstraint/distance(_:to:)-7yk7n.md)
  Creates a constraint that keeps a node within a certain distance of a point.
- [class func distance(SKRange, to: CGPoint, in: SKNode) -> Self](skconstraint/distance(_:to:in:).md)
  Creates a constraint that keeps a node within a certain distance of a point in another node’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint/distance(_:to:)-6507j)*