# getHue(_:saturation:brightness:alpha:)

**Framework**: AppKit  
**Kind**: method

Returns the color object’s HSB component and opacity values in the respective arguments.

**Availability**:
- macOS ?+

## Declaration

```swift
func getHue(_ hue: UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)
```

#### Discussion

If `NULL` is passed in as an argument, the method doesn’t set that value. This method works only with objects representing colors in the [`calibratedRGB`](nscolorspacename/calibratedrgb.md) or [`deviceRGB`](nscolorspacename/devicergb.md) color space. Sending it to other objects raises an exception.

## Parameters

- `hue`: Upon return, contains the hue component of the color object.
- `saturation`: Upon return, contains the saturation component of the color object.
- `brightness`: Upon return, contains the brightness component of the color object.
- `alpha`: Upon return, contains the opacity value of the color object.

## See Also

- [var brightnessComponent: CGFloat](nscolor/brightnesscomponent.md)
  The brightness component value of the color.
- [var hueComponent: CGFloat](nscolor/huecomponent.md)
  The hue component value of the color.
- [var alphaComponent: CGFloat](nscolor/alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var saturationComponent: CGFloat](nscolor/saturationcomponent.md)
  The saturation component value of the color.
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getcyan(_:magenta:yellow:black:alpha:).md)
  Returns the color object’s CMYK and opacity values.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getred(_:green:blue:alpha:).md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getwhite(_:alpha:).md)
  Returns the grayscale and alpha values of the color.
- [var numberOfComponents: Int](nscolor/numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](nscolor/getcomponents(_:).md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/gethue(_:saturation:brightness:alpha:))*