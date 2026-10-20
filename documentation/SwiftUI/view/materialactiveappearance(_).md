# materialActiveAppearance(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets an explicit active appearance for materials in this view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func materialActiveAppearance(_ appearance: MaterialActiveAppearance) -> some View
```

## See Also

### Transforming colors
- [func brightness(Double) -> some View](./brightness%28_%29.md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](./contrast%28_%29.md)
  Sets the contrast and separation between similar colors in this view.
- [func colorInvert() -> some View](./colorinvert%28%29.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](./colormultiply%28_%29.md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](./saturation%28_%29.md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](./grayscale%28_%29.md)
  Adds a grayscale effect to this view.
- [func hueRotation(Angle) -> some View](./huerotation%28_%29.md)
  Applies a hue rotation effect to this view.
- [func luminanceToAlpha() -> some View](./luminancetoalpha%28%29.md)
  Adds a luminance to alpha effect to this view.
- [var materialActiveAppearance: MaterialActiveAppearance](../environmentvalues/materialactiveappearance.md)
  The behavior materials should use for their active state, defaulting to `automatic`.
- [struct MaterialActiveAppearance](../materialactiveappearance.md)
  The behavior for how materials appear active and inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/materialactiveappearance(_:))*