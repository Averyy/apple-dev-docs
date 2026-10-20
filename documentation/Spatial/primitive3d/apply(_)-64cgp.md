# apply(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Applies a projective transform.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
mutating func apply(_ transform: ProjectiveTransform3D)
```

## Parameters

- `transform`: The projective transform that the function applies to the Spatial primitive.

## Default Implementations

### Primitive3D Implementations
- [func apply(ProjectiveTransform3D)](./apply%28_%29-2v2n0.md)
  Applies a projective transform.
- [func apply(AffineTransform3D)](./apply%28_%29-5lutp.md)
  Applies an affine transform.
- [func apply(Pose3D)](./apply%28_%29-5syk0.md)

## See Also

### Transforming primitives
- [func apply(AffineTransform3D)](./apply%28_%29-1nv9y.md)
  Applies an affine transform.
- [func applying(AffineTransform3D) -> Self](./applying%28_%29-6264n.md)
  Returns the entity that results from applying an affine transform.
- [func applying(ProjectiveTransform3D) -> Self](./applying%28_%29-6icvg.md)
  Returns the entity that results from applying a projective transform.
- [func apply(Pose3D)](./apply%28_%29-4ic73.md)
  Applies a pose.
- [func applying(Pose3D) -> Self](./applying%28_%29-5yia.md)
  Returns the entity that results from applying a pose.
- [func unapply(AffineTransform3D)](./unapply%28_%29-4z6og.md)
  Unapplies an affine transform.
- [func unapply(ProjectiveTransform3D)](./unapply%28_%29-5haxp.md)
  Unapplies a projective transform.
- [func unapplying(AffineTransform3D) -> Self](./unapplying%28_%29-8ihh5.md)
  Returns the entity that results from unapplying an affine transform.
- [func unapplying(ProjectiveTransform3D) -> Self](./unapplying%28_%29-5ppqi.md)
  Returns the entity that results from unapplying a projective transform.
- [func unapply(Pose3D)](./unapply%28_%29-2992s.md)
  Unapplies a pose.
- [func unapplying(Pose3D) -> Self](./unapplying%28_%29-37fbg.md)
  Returns the entity that results from unapplying a pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3d/apply(_:)-64cgp)*