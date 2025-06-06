# rotation3DEffect(_:axis:anchor:)

**Framework**: Assignables  
**Kind**: method

Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.

**Availability**:
- visionOS 1.0+ - Deprecated

## Declaration

```swift
nonisolated
func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> some View
```

#### Return Value

A view with rotated content.

#### Discussion

This modifier rotates the view’s content without changing the view’s frame. The following code displays a 3D model with a rotation of 45° about the y-axis using the default anchor point at the center of the view:

```None
Model3D(named: "robot")
    .rotation3DEffect(.degrees(45), axis: .y)
```

## Parameters

- `angle`: The angle by which to rotate the view’s content.
- `axis`: The axis of rotation.
- `anchor`: The unit point within the view about which to perform   the rotation. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/rotation3deffect(_:axis:anchor:)-208v0)*