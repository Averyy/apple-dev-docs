# brightness(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Brightens the view by the specified amount.

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
func brightness(_ amount: Double) -> some VisualEffect
```

#### Return Value

An effect that brightens the view by the specified amount.

## Parameters

- `amount`: A value between 0 (no effect) and 1 (full white brightening) that represents the intensity of the brightness effect.

## See Also

### Adjusting Color
- [func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect](./coloreffect%28_,isenabled%29.md)
  Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func contrast(Double) -> some VisualEffect](./contrast%28_%29.md)
  Sets the contrast and separation between similar colors in the view.
- [func grayscale(Double) -> some VisualEffect](./grayscale%28_%29.md)
  Adds a grayscale effect to the view.
- [func hueRotation(Angle) -> some VisualEffect](./huerotation%28_%29.md)
  Applies a hue rotation effect to the view.
- [func saturation(Double) -> some VisualEffect](./saturation%28_%29.md)
  Adjusts the color saturation of the view.
- [func opacity(Double) -> some VisualEffect](./opacity%28_%29.md)
  Sets the transparency of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/brightness(_:))*