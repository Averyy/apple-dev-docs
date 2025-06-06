# transformEffect(_:)

**Framework**: FamilyControls  
**Kind**: method

Applies an affine transformation to this view’s rendered output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transformEffect(_ transform: CGAffineTransform) -> some View
```

#### Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of the view according to the provided [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform).

In the example below, the text is rotated at -30˚ on the `y` axis.

```swift
let transform = CGAffineTransform(rotationAngle: -30 * (.pi / 180))

Text("Projection effect using transforms")
    .transformEffect(transform)
    .border(Color.gray)
```

## Parameters

- `transform`: A    to   apply to the view.

## See Also

- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](familyactivitypicker/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](familyactivitypicker/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func projectionEffect(ProjectionTransform) -> some View](familyactivitypicker/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/transformeffect(_:))*