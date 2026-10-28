# rotation3DEffect(_:axis:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.

**Availability**:
- visionOS 1.0+ - Deprecated

## Declaration

```swift
@export(implementation)
nonisolated func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func rotation3DEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D = .center) -> some View
```

```swift
@export(implementation)
nonisolated func rotation3DEffect(_ angle: Angle, axis: RotationAxis3D, anchor: UnitPoint3D = .center) -> ModifiedContent<Self, _Rotation3DEffectAngleAxis>
```

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame. The following code displays a 3D model with a rotation of 45° about the y-axis using the default anchor point at the center of the view:

```swift
Model3D(named: "robot")
    .rotation3DEffect(.degrees(45), axis: .y)
```

## Parameters

- `angle`: The angle by which to rotate the view’s content.
- `axis`: The axis of rotation.
- `anchor`: The unit point within the view about which to perform the rotation. The default value is [`center`](../unitpoint3d/center.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/rotation3deffect(_:axis:anchor:)-8vi88)*