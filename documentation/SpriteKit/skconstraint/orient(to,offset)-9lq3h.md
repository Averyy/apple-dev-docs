# orient(to:offset:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a constraint that forces a node to rotate to face a fixed point.

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
class func orient(to point: CGPoint, offset radians: SKRange) -> Self
```

```objc
+ (instancetype) orientToPoint:(CGPoint) point offset:(SKRange *) radians;
```

#### Return Value

A new constraint.

#### Discussion

Each time when constraints are applied, a new angle is calculated so that a line projected at this angle would point at the target point. This angle is added to the values specified in the `radians` property to create a new range. Finally, the node’s [`zRotation`](../sknode/zrotation.md) value is clamped to fit inside this range.

## Parameters

- `point`: A point in the node’s parent’s coordinate system.
- `radians`: An offset that is added to the [`zRotation`](../sknode/zrotation.md) value after it is calculated.

## See Also

### Creating Orientation Constraints
- [Creating a Look-At Constraint](../creating-a-look-at-constraint.md)
  Make a node automatically rotate itself based on the changing position of another node, by using orientation constraints.
- [class func orient(to: SKNode, offset: SKRange) -> Self](./orient%28to,offset%29-1h1tw.md)
  Creates a constraint that forces a node to rotate to face another node.
- [class func orient(to: CGPoint, in: SKNode, offset: SKRange) -> Self](./orient%28to,in,offset%29.md)
  Creates a constraint that forces a node to rotate to face a point in another node’s coordinate system.
- [class func zRotation(SKRange) -> Self](./zrotation%28_%29.md)
  Creates a constraint that limits the orientation of a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint/orient(to:offset:)-9lq3h)*