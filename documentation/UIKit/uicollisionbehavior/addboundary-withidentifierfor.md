# addBoundary(withIdentifier:for:)

**Framework**: UIKit  
**Kind**: method

Adds a collision boundary, specified as a Bezier path, to the collision behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addBoundary(withIdentifier identifier: any NSCopying, for bezierPath: UIBezierPath)
```

## Parameters

- `identifier`: An arbitrary identifier for the boundary you are adding.
- `bezierPath`: The coordinate system and origin point for the path depend on how you’ve initialized the dynamic animator (that you’re adding the behavior to). See the overview in   for more information.

## See Also

- [func addBoundary(withIdentifier: any NSCopying, from: CGPoint, to: CGPoint)](uicollisionbehavior/addboundary(withidentifier:from:to:).md)
  Adds a collision boundary, specified as a line segment, to the collision behavior.
- [var boundaryIdentifiers: [any NSCopying]?](uicollisionbehavior/boundaryidentifiers.md)
  The set of boundary identifiers that you’ve added to the collision behavior.
- [func boundary(withIdentifier: any NSCopying) -> UIBezierPath?](uicollisionbehavior/boundary(withidentifier:).md)
  Returns a specified Bezier-path boundary.
- [var collisionMode: UICollisionBehavior.Mode](uicollisionbehavior/collisionmode.md)
  The type of edges that participate in collisions for the collision behavior.
- [func removeAllBoundaries()](uicollisionbehavior/removeallboundaries.md)
  Removes all previously-specified collision boundaries from the collision behavior.
- [func removeBoundary(withIdentifier: any NSCopying)](uicollisionbehavior/removeboundary(withidentifier:).md)
  Removes a specific collision boundary from the collision behavior.
- [func setTranslatesReferenceBoundsIntoBoundary(with: UIEdgeInsets)](uicollisionbehavior/settranslatesreferenceboundsintoboundary(with:).md)
  Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.
- [var translatesReferenceBoundsIntoBoundary: Bool](uicollisionbehavior/translatesreferenceboundsintoboundary.md)
  Specifies whether a boundary based on the reference system is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/addboundary(withidentifier:for:))*