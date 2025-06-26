# colorInvert()

**Framework**: FamilyControls  
**Kind**: method

Inverts the colors in this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
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

## See Also

- [func blur(radius: CGFloat, opaque: Bool) -> some View](familyactivitypicker/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func opacity(Double) -> some View](familyactivitypicker/opacity(_:).md)
  Sets the transparency of this view.
- [func brightness(Double) -> some View](familyactivitypicker/brightness(_:).md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](familyactivitypicker/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func colorMultiply(Color) -> some View](familyactivitypicker/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](familyactivitypicker/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](familyactivitypicker/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func hueRotation(Angle) -> some View](familyactivitypicker/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func luminanceToAlpha() -> some View](familyactivitypicker/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/colorinvert())*