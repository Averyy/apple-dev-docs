# addBoundary(withIdentifier:from:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a collision boundary, specified as a line segment, to the collision behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func addBoundary(withIdentifier identifier: any NSCopying, from p1: CGPoint, to p2: CGPoint)
```

```objc
- (void) addBoundaryWithIdentifier:(id<NSCopying>) identifier fromPoint:(CGPoint) p1 toPoint:(CGPoint) p2;
```

## Discussion

This is a convenience method based on the [`addBoundary(withIdentifier:for:)`](./addboundary%28withidentifier,for%29.md) method. The coordinate system and origin point for the `p1` and `p2` parameters depend on how you’ve initialized the dynamic animator (that you’re adding the behavior to). See the overview in [`UIDynamicAnimator`](../uidynamicanimator.md) for more information.

## Parameters

- `identifier`: An arbitrary identifier for the boundary you are adding.
- `p1`: The starting point for the boundary line segment.
- `p2`: The ending point for the boundary line segment.

## See Also

### Configuring a collision behavior
- [func addBoundary(withIdentifier: any NSCopying, for: UIBezierPath)](./addboundary%28withidentifier,for%29.md)
  Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [var boundaryIdentifiers: [any NSCopying]?](./boundaryidentifiers.md)
  The set of boundary identifiers that you’ve added to the collision behavior.
- [func boundary(withIdentifier: any NSCopying) -> UIBezierPath?](./boundary%28withidentifier%29.md)
  Returns a specified Bezier-path boundary.
- [var collisionMode: UICollisionBehavior.Mode](./collisionmode.md)
  The type of edges that participate in collisions for the collision behavior.
- [func removeAllBoundaries()](./removeallboundaries%28%29.md)
  Removes all previously-specified collision boundaries from the collision behavior.
- [func removeBoundary(withIdentifier: any NSCopying)](./removeboundary%28withidentifier%29.md)
  Removes a specific collision boundary from the collision behavior.
- [func setTranslatesReferenceBoundsIntoBoundary(with: UIEdgeInsets)](./settranslatesreferenceboundsintoboundary%28with%29.md)
  Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.
- [var translatesReferenceBoundsIntoBoundary: Bool](./translatesreferenceboundsintoboundary.md)
  Specifies whether a boundary based on the reference system is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/addboundary(withidentifier:from:to:))*