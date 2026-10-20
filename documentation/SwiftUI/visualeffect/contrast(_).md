# contrast(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the contrast and separation between similar colors in the view.

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
func contrast(_ amount: Double) -> some VisualEffect
```

#### Return Value

An effect that applies color contrast to the view.

#### Discussion

Apply contrast to a view to increase or decrease the separation between similar colors in the view.

## Parameters

- `amount`: The intensity of color contrast to apply. negative values invert colors in addition to applying contrast.

## See Also

### Adjusting Color
- [func brightness(Double) -> some VisualEffect](./brightness%28_%29.md)
  Brightens the view by the specified amount.
- [func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect](./coloreffect%28_,isenabled%29.md)
  Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func grayscale(Double) -> some VisualEffect](./grayscale%28_%29.md)
  Adds a grayscale effect to the view.
- [func hueRotation(Angle) -> some VisualEffect](./huerotation%28_%29.md)
  Applies a hue rotation effect to the view.
- [func saturation(Double) -> some VisualEffect](./saturation%28_%29.md)
  Adjusts the color saturation of the view.
- [func opacity(Double) -> some VisualEffect](./opacity%28_%29.md)
  Sets the transparency of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/contrast(_:))*