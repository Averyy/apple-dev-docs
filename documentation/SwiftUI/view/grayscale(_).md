# grayscale(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a grayscale effect to this view.

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
func grayscale(_ amount: Double) -> some View
```

## Return Value

A view that adds a grayscale effect to this view.

## Discussion

A grayscale effect reduces the intensity of colors in this view.

The example below shows a series of red squares with their grayscale effect increasing from 0 (reddest) to 99% (fully desaturated) in approximate 20% increments:

```swift
struct Saturation: View {
    var body: some View {
        HStack {
            ForEach(0..<6) {
                Color.red.frame(width: 60, height: 60, alignment: .center)
                    .grayscale(Double($0) * 0.1999)
                    .overlay(Text("\(Double($0) * 0.1999 * 100, specifier: "%.4f")%"),
                             alignment: .bottom)
                    .border(Color.gray)
            }
        }
    }
}
```

![Rendering showing the effects of grayscale adjustments in](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-grayscale@2x.png)

## Parameters

- `amount`: The intensity of grayscale to apply from 0.0 to less than 1.0. Values closer to 0.0 are more colorful, and values closer to 1.0 are less colorful.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/grayscale(_:))*