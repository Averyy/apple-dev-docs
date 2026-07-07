# rotation3DEffect(_:axis:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Rotates content by an angle about an axis that you specify as a rotation axis value.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> some VisualEffect
```

#### Return Value

A rotation effect.

#### Discussion

This effect causes the content to appear rotated, but doesn’t change the content’s frame. The following code applies a rotation of 45° about the y-axis, using the default anchor point at the center of the content:

```swift
Model3D(named: "robot")
    .visualEffect { content, geometryProxy in
        content
            .rotation3DEffect(.degrees(45), axis: .y)
    }
```

## Parameters

- `angle`: The angle by which to rotate the view’s content.
- `axis`: The axis of rotation.
- `anchor`: The unit point within the content about which to perform the rotation. The default value is [`center`](unitpoint3d/center.md).

## See Also

- [func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect](visualeffect/rotationeffect(_:anchor:).md)
  Rotates content in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some VisualEffect](visualeffect/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect](visualeffect/perspectiverotationeffect(_:axis:anchor:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect](visualeffect/rotation3deffect(_:anchor:).md)
  Rotates content by the specified 3D rotation value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/rotation3deffect(_:axis:anchor:))*