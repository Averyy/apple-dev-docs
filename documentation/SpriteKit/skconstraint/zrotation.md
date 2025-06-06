# zRotation(_:)

**Framework**: SpriteKit  
**Kind**: method

Creates a constraint that limits the orientation of a node.

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
class func zRotation(_ zRange: SKRange) -> Self
```

## Mentions

- [Creating a Look-At Constraint](creating-a-look-at-constraint.md)

#### Return Value

A new constraint.

#### Discussion

Each time when constraints are applied, the node’s [`zRotation`](sknode/zrotation.md) property is clamped so that it is within the specified range.

## Parameters

- `zRange`: A range value that specifies the minimum and maximum values of the node’s   property.

## See Also

- [Creating a Look-At Constraint](creating-a-look-at-constraint.md)
  Make a node automatically rotate itself based on the changing position of another node, by using orientation constraints.
- [class func orient(to: SKNode, offset: SKRange) -> Self](skconstraint/orient(to:offset:)-1h1tw.md)
  Creates a constraint that forces a node to rotate to face another node.
- [class func orient(to: CGPoint, offset: SKRange) -> Self](skconstraint/orient(to:offset:)-9lq3h.md)
  Creates a constraint that forces a node to rotate to face a fixed point.
- [class func orient(to: CGPoint, in: SKNode, offset: SKRange) -> Self](skconstraint/orient(to:in:offset:).md)
  Creates a constraint that forces a node to rotate to face a point in another node’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint/zrotation(_:))*