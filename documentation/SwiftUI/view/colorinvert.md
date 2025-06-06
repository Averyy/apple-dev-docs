# colorInvert()

**Framework**: SwiftUI  
**Kind**: method

Inverts the colors in this view.

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
func colorInvert() -> some View
```

#### Return Value

A view that inverts its colors.

#### Discussion

The `colorInvert()` modifier inverts all of the colors in a view so that each color displays as its complementary color. For example, blue converts to yellow, and white converts to black.

In the example below, two red squares each have an interior green circle. The inverted square shows the effect of the square’s colors: complimentary colors for red and green — teal and purple.

```swift
struct InnerCircleView: View {
    var body: some View {
        Circle()
            .fill(Color.green)
            .frame(width: 40, height: 40, alignment: .center)
    }
}

struct ColorInvert: View {
    var body: some View {
        HStack {
            Color.red.frame(width: 100, height: 100, alignment: .center)
                .overlay(InnerCircleView(), alignment: .center)
                .overlay(Text("Normal")
                             .font(.callout),
                         alignment: .bottom)
                .border(Color.gray)

            Spacer()

            Color.red.frame(width: 100, height: 100, alignment: .center)
                .overlay(InnerCircleView(), alignment: .center)
                .colorInvert()
                .overlay(Text("Inverted")
                             .font(.callout),
                         alignment: .bottom)
                .border(Color.gray)
        }
        .padding(50)
    }
}
```

![Two red squares with centered green circles with one showing the](https://docs-assets.developer.apple.com/published/091a4b24f901b1d02e956ed751784899/SwiftUI-View-colorInvert%402x.png)

## See Also

- [func brightness(Double) -> some View](view/brightness(_:).md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](view/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func colorMultiply(Color) -> some View](view/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](view/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](view/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func hueRotation(Angle) -> some View](view/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func luminanceToAlpha() -> some View](view/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](view/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [var materialActiveAppearance: MaterialActiveAppearance](environmentvalues/materialactiveappearance.md)
  The behavior materials should use for their active state, defaulting to `automatic`.
- [struct MaterialActiveAppearance](materialactiveappearance.md)
  The behavior for how materials appear active and inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/colorinvert())*