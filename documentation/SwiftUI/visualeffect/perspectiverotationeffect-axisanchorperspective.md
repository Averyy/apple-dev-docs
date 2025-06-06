# perspectiveRotationEffect(_:axis:anchor:perspective:)

**Framework**: SwiftUI  
**Kind**: method

Renders content as if it’s rotated in three dimensions around the specified axis.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func perspectiveRotationEffect(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D = .back, perspective: CGFloat = 1) -> some VisualEffect
```

#### Return Value

A rotation effect.

#### Discussion

Use this method to create the effect of rotating content in three dimensions around a specified axis of rotation. The modifier projects two dimensional content onto the original content’s plane. Use the `perspective` input to control the renderer’s vanishing point. The following example creates the appearance of rotating text 45˚ about the y-axis:

```swift
Text("Rotation by passing an angle in degrees")
    .visualEffect { content, geometryProxy in
        content
            .perspectiveRotationEffect(
                .degrees(45),
                axis: (x: 0.0, y: 1.0, z: 0.0),
                anchor: .center,
                perspective: 1)
        }
    .border(Color.gray)
```

![A screenshot of text in a grey box. The text says Rotation by passing an angle in degrees. The text is rendered in a way that makes it appear farther from the viewer on the right side and closer on the left, as if the text is angled to face someone sitting on the viewer’s right.](https://docs-assets.developer.apple.com/published/26dcde23639ed248bfc573a1a0986072/SwiftUI-View-rotation3DEffect%402x.png)

> ❗ **Important**: To truly rotate content in three dimensions, use a 3D rotation effect without a perspective input like [`rotation3DEffect(_:axis:anchor:)`](visualeffect/rotation3deffect(_:axis:anchor:).md).

To truly rotate content in three dimensions, use a 3D rotation effect without a perspective input like [`rotation3DEffect(_:axis:anchor:)`](visualeffect/rotation3deffect(_:axis:anchor:).md).

## Parameters

- `angle`: The angle by which to rotate the content.
- `axis`: The axis of rotation, specified as a tuple with named   elements for each of the three spatial dimensions.
- `anchor`: A unit point within the content about which to perform   the rotation. The default value is  .
- `perspective`: The relative vanishing point for the rotation. The   default is  .

## See Also

- [func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect](visualeffect/rotationeffect(_:anchor:).md)
  Rotates content in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some VisualEffect](visualeffect/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect](visualeffect/rotation3deffect(_:anchor:).md)
  Rotates content by the specified 3D rotation value.
- [func rotation3DEffect(_:axis:anchor:)](visualeffect/rotation3deffect(_:axis:anchor:).md)
  Rotates content by an angle about an axis that you specify as a tuple of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/perspectiverotationeffect(_:axis:anchor:perspective:))*