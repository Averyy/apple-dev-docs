# rotation3DEffect(_:axis:anchor:)

**Framework**: Assignables  
**Kind**: method

Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> ModifiedContent<Self, _Rotation3DEffectAngleAxis>
```

#### Return Value

A view with rotated content.

#### Discussion

> **Note**: During an animation, the angle and each element of the axis is interpolated separately, which may cause undesirable results. To achieve more natural animations, consider using `View/rotation3DEffect(_:anchor:)`

During an animation, the angle and each element of the axis is interpolated separately, which may cause undesirable results. To achieve more natural animations, consider using `View/rotation3DEffect(_:anchor:)`

This modifier rotates the view’s content without changing the view’s frame. The following code displays a 3D model with a rotation of 45° about the y-axis using the default anchor point at the center of the view:

```None
Model3D(named: "robot")
    .rotation3DEffect(.degrees(45), axis: .y)
```

> **Note**: The following example is not equivalent to the previous. This example will use spherical linear interpolation during an animation.

The following example is not equivalent to the previous. This example will use spherical linear interpolation during an animation.

```swift
Model3D(named: "robot")
    .rotation3DEffect(Rotation3D(.init(degrees: 45), axis: .y)
```

## Parameters

- `angle`: The angle by which to rotate the view’s content.
- `axis`: The axis of rotation.
- `anchor`: The unit point within the view about which to perform   the rotation. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/rotation3deffect(_:axis:anchor:)-26k0z)*