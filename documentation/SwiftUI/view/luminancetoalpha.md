# luminanceToAlpha()

**Framework**: SwiftUI  
**Kind**: method

Adds a luminance to alpha effect to this view.

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
func luminanceToAlpha() -> some View
```

#### Return Value

A view with the luminance to alpha effect applied.

#### Discussion

Use this modifier to create a semitransparent mask, with the opacity of each part of the modified view controlled by the luminance of the corresponding part of the original view. Regions of lower luminance become more transparent, while higher luminance yields greater opacity.

In particular, the modifier maps the red, green, and blue components of each input pixel’s color to a grayscale value, and that value becomes the alpha component of a black pixel in the output. This modifier produces an effect that’s equivalent to using the `feColorMatrix` filter primitive with the `luminanceToAlpha` type attribute, as defined by the [`Scalable Vector Graphics (SVG) 2`](https://developer.apple.comhttps://www.w3.org/TR/SVG2/) specification.

The example below defines a `Palette` view as a series of rectangles, each composed as a [`Color`](color.md) with a particular white value, and then displays two versions of the palette over a blue background:

```swift
struct Palette: View {
    var body: some View {
        HStack(spacing: 0) {
            ForEach(0..<10) { index in
                Color(white: Double(index) / Double(9))
                    .frame(width: 20, height: 40)
            }
        }
    }
}

struct LuminanceToAlphaExample: View {
    var body: some View {
        VStack(spacing: 20) {
            Palette()

            Palette()
                .luminanceToAlpha()
        }
        .padding()
        .background(.blue)
    }
}
```

The unmodified version of the palette contains rectangles that range from solid black to solid white, thus with increasing luminance. The second version of the palette, which has the `luminanceToAlpha()` modifier applied, allows the background to show through in an amount that corresponds inversely to the luminance of the input.

![A screenshot of a blue background with two wide rectangles on it,](https://docs-assets.developer.apple.com/published/e2c3c9501978adf4162289344ce36c3a/View-luminanceToAlpha-1-iOS%402x.png)

## See Also

- [func brightness(Double) -> some View](view/brightness(_:).md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](view/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func colorInvert() -> some View](view/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](view/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](view/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](view/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func hueRotation(Angle) -> some View](view/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](view/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [var materialActiveAppearance: MaterialActiveAppearance](environmentvalues/materialactiveappearance.md)
  The behavior materials should use for their active state, defaulting to `automatic`.
- [struct MaterialActiveAppearance](materialactiveappearance.md)
  The behavior for how materials appear active and inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/luminancetoalpha())*