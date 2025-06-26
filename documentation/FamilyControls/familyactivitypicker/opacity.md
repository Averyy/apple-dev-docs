# opacity(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the transparency of this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func opacity(_ opacity: Double) -> some View
```

#### Return Value

A view that sets the transparency of this view.

#### Discussion

Apply opacity to reveal views that are behind another view or to de-emphasize a view.

When applying the `opacity(_:)` modifier to a view that has already had its opacity transformed, the modifier multiplies the effect of the underlying opacity transformation.

The example below shows yellow and red rectangles configured to overlap. The top yellow rectangle has its opacity set to 50%, allowing the occluded portion of the bottom rectangle to be visible:

```swift
struct Opacity: View {
    var body: some View {
        VStack {
            Color.yellow.frame(width: 100, height: 100, alignment: .center)
                .zIndex(1)
                .opacity(0.5)

            Color.red.frame(width: 100, height: 100, alignment: .center)
                .padding(-40)
        }
    }
}
```

## Parameters

- `opacity`: A value between 0 (fully transparent) and 1 (fully   opaque).

## See Also

- [func blur(radius: CGFloat, opaque: Bool) -> some View](familyactivitypicker/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
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
- [func hueRotation(Angle) -> some View](familyactivitypicker/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func luminanceToAlpha() -> some View](familyactivitypicker/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/opacity(_:))*