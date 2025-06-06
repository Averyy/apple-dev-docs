# hueRotation(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies a hue rotation effect to the view.

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
func hueRotation(_ angle: Angle) -> some VisualEffect
```

#### Return Value

An effect that shifts all of the colors in the view.

#### Discussion

Use hue rotation effect to shift all of the colors in a view according to the angle you specify.

## Parameters

- `angle`: The hue rotation angle to apply to the colors in the   view.

## See Also

- [func brightness(Double) -> some VisualEffect](visualeffect/brightness(_:).md)
  Brightens the view by the specified amount.
- [func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect](visualeffect/coloreffect(_:isenabled:).md)
  Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func contrast(Double) -> some VisualEffect](visualeffect/contrast(_:).md)
  Sets the contrast and separation between similar colors in the view.
- [func grayscale(Double) -> some VisualEffect](visualeffect/grayscale(_:).md)
  Adds a grayscale effect to the view.
- [func saturation(Double) -> some VisualEffect](visualeffect/saturation(_:).md)
  Adjusts the color saturation of the view.
- [func opacity(Double) -> some VisualEffect](visualeffect/opacity(_:).md)
  Sets the transparency of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/huerotation(_:))*