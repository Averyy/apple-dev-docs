# rotationEffect(_:anchor:)

**Framework**: FamilyControls  
**Kind**: method

Rotates a view’s rendered output in two dimensions around the specified point.

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
func rotationEffect(_ angle: Angle, anchor: UnitPoint = .center) -> some View
```

#### Return Value

A view with rotated content.

#### Discussion

This modifier rotates the view’s content around the axis that points out of the xy-plane. It has no effect on the view’s frame. The following code rotates text by 22˚ and then draws a border around the modified view to show that the frame remains unchanged by the rotation modifier:

```swift
Text("Rotation by passing an angle in degrees")
    .rotationEffect(.degrees(22))
    .border(Color.gray)
```

## Parameters

- `angle`: The angle by which to rotate the view.
- `anchor`: A unit point within the view about which to   perform the rotation. The default value is  .

## See Also

- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](familyactivitypicker/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func projectionEffect(ProjectionTransform) -> some View](familyactivitypicker/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func transformEffect(CGAffineTransform) -> some View](familyactivitypicker/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/rotationeffect(_:anchor:))*