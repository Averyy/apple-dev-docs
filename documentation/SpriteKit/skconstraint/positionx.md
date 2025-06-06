# positionX(_:)

**Framework**: SpriteKit  
**Kind**: method

Creates a constraint that restricts the x-coordinate of a node’s position.

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
class func positionX(_ range: SKRange) -> Self
```

## Mentions

- [Creating Position Constraints](creating-position-constraints.md)

#### Return Value

A new constraint.

#### Discussion

Each time constraints are applied, the x-coordinate of the node’s [`position`](sknode/position.md) property is clamped so that it lies inside the specified range.

## Parameters

- `range`: The range to restrict the coordinate to.

## See Also

- [Creating Position Constraints](creating-position-constraints.md)
  Create a position constraint and add it to a node.
- [class func positionX(SKRange, y: SKRange) -> Self](skconstraint/positionx(_:y:).md)
  Creates a constraint that restricts both coordinates of a node’s position.
- [class func positionY(SKRange) -> Self](skconstraint/positiony(_:).md)
  Creates a constraint that restricts the y-coordinate of a node’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint/positionx(_:))*