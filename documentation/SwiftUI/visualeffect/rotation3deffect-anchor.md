# rotation3DEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Rotates content by the specified 3D rotation value.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func rotation3DEffect(_ rotation: Rotation3D, anchor: UnitPoint3D = .center) -> some VisualEffect
```

#### Return Value

A rotation effect.

#### Discussion

This effect causes the content to appear rotated, but doesn’t change the content’s frame. The following code applies a rotation of 45° about the y-axis, using the default anchor point at the center of the content:

```swift
Model3D(named: "robot")
    .visualEffect { content, geometryProxy in
        content
            .rotation3DEffect(Rotation3D(angle: .degrees(45), axis: .y))
    }
```

During an animation, this modifier uses spherical linear interpolation, which produces more natural animations, but doesn’t support rotations over 360 degrees. To specify angles over 360 degrees, consider using `View/rotation3DEffect(_:axis:anchor:)-4enag`.

## Parameters

- `rotation`: A rotation to apply to the content.
- `anchor`: The unit point within the content about which to perform   the rotation. The default value is  .

## See Also

- [func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect](visualeffect/rotationeffect(_:anchor:).md)
  Rotates content in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some VisualEffect](visualeffect/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect](visualeffect/perspectiverotationeffect(_:axis:anchor:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(_:axis:anchor:)](visualeffect/rotation3deffect(_:axis:anchor:).md)
  Rotates content by an angle about an axis that you specify as a tuple of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/rotation3deffect(_:anchor:))*