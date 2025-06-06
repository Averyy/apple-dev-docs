# rotation3DEffect(_:anchor:)

**Framework**: Assignables  
**Kind**: method

Rotates the view’s content by the specified 3D rotation value.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func rotation3DEffect(_ rotation: Rotation3D, anchor: UnitPoint3D = .center) -> some View
```

#### Return Value

A view with rotated content.

#### Discussion

This modifier rotates the view’s content without changing the view’s frame. The following code displays a 3D model with a rotation of 45° about the y-axis using the default anchor point at the center of the view:

```None
Model3D(named: "robot")
    .rotation3DEffect(Rotation3D(angle: .degrees(45), axis: .y))
```

During an animation, this modifier uses spherical linear interpolation, which produces more natural animations, but doesn’t support rotations over 360 degrees. To specify angles over 360 degrees, consider using `View/rotation3DEffect(_:axis:anchor:)-4enag`.

## Parameters

- `rotation`: A rotation to apply to the view’s content.
- `anchor`: The unit point within the view about which to perform   the rotation. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/rotation3deffect(_:anchor:))*