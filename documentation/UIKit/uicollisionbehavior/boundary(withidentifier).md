# boundary(withIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a specified Bezier-path boundary.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func boundary(withIdentifier identifier: any NSCopying) -> UIBezierPath?
```

```objc
- (UIBezierPath *) boundaryWithIdentifier:(id<NSCopying>) identifier;
```

#### Return Value

A Bezier-path boundary.

## Parameters

- `identifier`: A boundary identifier that you’ve previously added to the collision behavior.

## See Also

### Configuring a collision behavior
- [func addBoundary(withIdentifier: any NSCopying, for: UIBezierPath)](./addboundary%28withidentifier,for%29.md)
  Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [func addBoundary(withIdentifier: any NSCopying, from: CGPoint, to: CGPoint)](./addboundary%28withidentifier,from,to%29.md)
  Adds a collision boundary, specified as a line segment, to the collision behavior.
- [var boundaryIdentifiers: [any NSCopying]?](./boundaryidentifiers.md)
  The set of boundary identifiers that you’ve added to the collision behavior.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/boundary(withidentifier:))*