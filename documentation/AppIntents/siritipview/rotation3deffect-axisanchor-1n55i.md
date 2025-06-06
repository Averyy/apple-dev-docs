# rotation3DEffect(_:axis:anchor:)

**Framework**: App Intents  
**Kind**: method

Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func rotation3DEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D = .center) -> some View
```

#### Return Value

A view with rotated content.

#### Discussion

> **Note**: During an animation, the angle and each element of the axis is interpolated separately, which may cause undesirable results. To achive more natual animations, cosinder using `View/rotation3DEffect(_:anchor:)`

During an animation, the angle and each element of the axis is interpolated separately, which may cause undesirable results. To achive more natual animations, cosinder using `View/rotation3DEffect(_:anchor:)`

This modifier rotates the view’s content without changing the view’s frame. The following code displays a 3D model with a rotation of 45° about the y-axis using the default anchor point at the center of the view:

```swift
Model3D(named: "robot")
    .rotation3DEffect(.degrees(45), axis: (x: 0, y: 1, z: 0))
```

> **Note**: The following example is not equivalent to the previous. This example will use spherical linear interpolation during an animation.

The following example is not equivalent to the previous. This example will use spherical linear interpolation during an animation.

```swift
let rotation = Rotation3D(
    .init(degrees: 45), axis: RotationAxis3D(x: 0, y: 1, z: 0))
Model3D(named: "robot")
    .rotation3DEffect(rotation)
```

## Parameters

- `angle`: The angle by which to rotate the view’s content.
- `axis`: The axis of rotation, specified as a tuple with named   elements for each of the three spatial dimensions.
- `anchor`: The unit point within the view about which to perform   the rotation. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/rotation3deffect(_:axis:anchor:)-1n55i)*