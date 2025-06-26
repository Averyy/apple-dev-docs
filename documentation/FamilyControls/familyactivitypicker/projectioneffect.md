# projectionEffect(_:)

**Framework**: FamilyControls  
**Kind**: method

Applies a projection transformation to this view’s rendered output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func projectionEffect(_ transform: ProjectionTransform) -> some View
```

#### Discussion

Use `projectionEffect(_:)` to apply a 3D transformation to the view.

The example below rotates the text 30˚ around the `z` axis, which is the axis pointing out of the screen:

```swift
// This transform represents a 30˚ rotation around the z axis.
let transform = CATransform3DMakeRotation(
    -30 * (.pi / 180), 0.0, 0.0, 1.0)

Text("Projection effects using transforms")
    .projectionEffect(.init(transform))
    .border(Color.gray)
```

## Parameters

- `transform`: A   to apply to the view.

## See Also

- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](familyactivitypicker/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](familyactivitypicker/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func transformEffect(CGAffineTransform) -> some View](familyactivitypicker/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/projectioneffect(_:))*