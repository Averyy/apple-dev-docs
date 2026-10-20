# brightness(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Brightens this view by the specified amount.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func brightness(_ amount: Double) -> some View
```

#### Return Value

A view that brightens this view by the specified amount.

#### Discussion

Use `brightness(_:)` to brighten the intensity of the colors in a view. The example below shows a series of red squares, with their brightness increasing from 0 (fully red) to 100% (white) in 20% increments.

```swift
struct Brightness: View {
    var body: some View {
        HStack {
            ForEach(0..<6) {
                Color.red.frame(width: 60, height: 60, alignment: .center)
                    .brightness(Double($0) * 0.2)
                    .overlay(Text("\(Double($0) * 0.2 * 100, specifier: "%.0f")%"),
                             alignment: .bottom)
                    .border(Color.gray)
            }
        }
    }
}
```

![Rendering showing the effects of brightness adjustments in 20%](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-brightness@2x.png)

## Parameters

- `amount`: A value between 0 (no effect) and 1 (full white brightening) that represents the intensity of the brightness effect.

## See Also

### Transforming colors
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
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](./materialactiveappearance%28_%29.md)
  Sets an explicit active appearance for materials in this view.
- [var materialActiveAppearance: MaterialActiveAppearance](../environmentvalues/materialactiveappearance.md)
  The behavior materials should use for their active state, defaulting to `automatic`.
- [struct MaterialActiveAppearance](../materialactiveappearance.md)
  The behavior for how materials appear active and inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/brightness(_:))*