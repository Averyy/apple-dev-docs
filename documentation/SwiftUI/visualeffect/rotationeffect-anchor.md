# rotationEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Rotates content in two dimensions around the specified point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func rotationEffect(_ angle: Angle, anchor: UnitPoint = .center) -> some VisualEffect
```

#### Return Value

A rotation effect.

#### Discussion

This effect rotates the content around the axis that points out of the xy-plane. It has no effect on the content’s frame. The following code rotates text by 22˚ and then draws a border around the modified view to show that the frame remains unchanged by the rotation:

```swift
Text("Rotation by passing an angle in degrees")
    .visualEffect { content, geometryProxy in
        content
            .rotationEffect(.degrees(22))
    }
    .border(Color.gray)
```

![A screenshot of text and a wide grey box. The text says Rotation by passing an angle in degrees. The baseline of the text is rotated clockwise by 22 degrees relative to the box. The center of the box and the center of the text are aligned.](https://docs-assets.developer.apple.com/published/b37c8f57cc3cc583b004f632134572e5/SwiftUI-View-rotationEffect%402x.png)

## Parameters

- `angle`: The angle by which to rotate the content.
- `anchor`: A unit point within the content about which to   perform the rotation. The default value is  .

## See Also

- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some VisualEffect](visualeffect/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect](visualeffect/perspectiverotationeffect(_:axis:anchor:perspective:).md)
  Renders content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect](visualeffect/rotation3deffect(_:anchor:).md)
  Rotates content by the specified 3D rotation value.
- [func rotation3DEffect(_:axis:anchor:)](visualeffect/rotation3deffect(_:axis:anchor:).md)
  Rotates content by an angle about an axis that you specify as a tuple of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/rotationeffect(_:anchor:))*