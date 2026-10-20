# setTranslatesReferenceBoundsIntoBoundary(with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTranslatesReferenceBoundsIntoBoundary(with insets: UIEdgeInsets)
```

```objc
- (void) setTranslatesReferenceBoundsIntoBoundaryWithInsets:(UIEdgeInsets) insets;
```

#### Discussion

The result of using this method depends on how you’ve initialized the dynamic animator (of class [`UIDynamicAnimator`](../uidynamicanimator.md)) that you’ve added the collision behavior to. See the overview in [`UIDynamicAnimator`](../uidynamicanimator.md) for a discussion of initialization options and modes for animators.

Here is how the dynamic animator’s initialization impacts use of this method:

- For a view-only dynamic animator, the reference bounds are those of the reference view
- For a collection-view dynamic animator, the reference bounds are those of the collection view layout
- For a dynamic-item dynamic animator, there are no reference bounds.

For a collision behavior added to a view-only or collection-view dynamic animator, activate a reference-system-based collision boundary by setting the [`translatesReferenceBoundsIntoBoundary`](./translatesreferenceboundsintoboundary.md) property to [`true`](../../Swift/true.md).

## Parameters

- `insets`: Insets to apply to the reference system’s bounds when defining the collision boundary.

## See Also

### Configuring a collision behavior
- [func addBoundary(withIdentifier: any NSCopying, for: UIBezierPath)](./addboundary%28withidentifier,for%29.md)
  Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [func addBoundary(withIdentifier: any NSCopying, from: CGPoint, to: CGPoint)](./addboundary%28withidentifier,from,to%29.md)
  Adds a collision boundary, specified as a line segment, to the collision behavior.
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
- [var translatesReferenceBoundsIntoBoundary: Bool](./translatesreferenceboundsintoboundary.md)
  Specifies whether a boundary based on the reference system is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/settranslatesreferenceboundsintoboundary(with:))*