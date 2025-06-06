# colorEffect(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func colorEffect(_ shader: Shader, isEnabled: Bool = true) -> some VisualEffect
```

#### Return Value

A new view that renders `self` with the shader applied as a color filter.

#### Discussion

For a shader function to act as a color filter it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, half4 color, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader and `color` its source color, as a pre-multiplied color in the destination color space. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the modified color value.

> ❗ **Important**: Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

## Parameters

- `shader`: The shader to apply to   as a color filter.
- `isEnabled`: Whether the effect is enabled or not.

## See Also

- [func brightness(Double) -> some VisualEffect](visualeffect/brightness(_:).md)
  Brightens the view by the specified amount.
- [func contrast(Double) -> some VisualEffect](visualeffect/contrast(_:).md)
  Sets the contrast and separation between similar colors in the view.
- [func grayscale(Double) -> some VisualEffect](visualeffect/grayscale(_:).md)
  Adds a grayscale effect to the view.
- [func hueRotation(Angle) -> some VisualEffect](visualeffect/huerotation(_:).md)
  Applies a hue rotation effect to the view.
- [func saturation(Double) -> some VisualEffect](visualeffect/saturation(_:).md)
  Adjusts the color saturation of the view.
- [func opacity(Double) -> some VisualEffect](visualeffect/opacity(_:).md)
  Sets the transparency of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/coloreffect(_:isenabled:))*