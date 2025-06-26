# hueRotation(_:)

**Framework**: FamilyControls  
**Kind**: method

Applies a hue rotation effect to this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func hueRotation(_ angle: Angle) -> some View
```

#### Return Value

A view that applies a hue rotation effect to this view.

#### Discussion

Use hue rotation effect to shift all of the colors in a view according to the angle you specify.

The example below shows a series of squares filled with a linear gradient. Each square shows the effect of a 36˚ hueRotation (a total of 180˚ across the 5 squares) on the gradient:

```swift
struct HueRotation: View {
    var body: some View {
        HStack {
            ForEach(0..<6) {
                Rectangle()
                    .fill(.linearGradient(
                        colors: [.blue, .red, .green],
                        startPoint: .top, endPoint: .bottom))
                    .hueRotation((.degrees(Double($0 * 36))))
                    .frame(width: 60, height: 60, alignment: .center)
            }
        }
    }
}
```

## Parameters

- `angle`: The hue rotation angle to apply to the colors in this   view.

## See Also

- [func blur(radius: CGFloat, opaque: Bool) -> some View](familyactivitypicker/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func opacity(Double) -> some View](familyactivitypicker/opacity(_:).md)
  Sets the transparency of this view.
- [func brightness(Double) -> some View](familyactivitypicker/brightness(_:).md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](familyactivitypicker/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func colorInvert() -> some View](familyactivitypicker/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](familyactivitypicker/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](familyactivitypicker/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](familyactivitypicker/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func luminanceToAlpha() -> some View](familyactivitypicker/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/huerotation(_:))*