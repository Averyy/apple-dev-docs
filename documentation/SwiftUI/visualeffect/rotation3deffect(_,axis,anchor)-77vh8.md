# rotation3DEffect(_:axis:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Rotates content by an angle about an axis that you specify as a rotation axis value.

**Availability**:
- visionOS 2.0+ - Deprecated

## Declaration

```swift
@export(implementation)
func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> _Rotation3DEffectAngleAxis
```

**Other overloads**:

```swift
@export(implementation)
func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> some VisualEffect
```

```swift
func rotation3DEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D = .center) -> some VisualEffect
```

## Return Value

A rotation effect.

## Discussion

> **Note**: During an animation, the angle and each element of the axis is interpolated separately, which may cause undesirable results. To achieve more natural animations, consider using [`rotation3DEffect(_:anchor:)`](../view/rotation3deffect%28_,anchor%29.md)

This effect causes the content to appear rotated, but doesn’t change the content’s frame. The following code applies a rotation of 45° about the y-axis, using the default anchor point at the center of the content:

```swift
Model3D(named: "robot")
    .visualEffect { content, geometryProxy in
        content
            .rotation3DEffect(.degrees(45), axis: .y)
    }
```

> **Note**: The following example is not equivalent to the previous. This example will use spherical linear interpolation during an animation.

```swift
Model3D(named: "robot")
    .rotation3DEffect(
        Rotation3D(angle: .degrees(45), axis: .y))
```

## Parameters

- `angle`: The angle by which to rotate the view’s content.
- `axis`: The axis of rotation.
- `anchor`: The unit point within the content about which to perform the rotation. The default value is [`center`](../unitpoint3d/center.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/rotation3deffect(_:axis:anchor:)-77vh8)*