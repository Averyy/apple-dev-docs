# getRed(_:green:blue:alpha:)

**Framework**: AppKit  
**Kind**: method

Returns the color object’s RGB component and opacity values in the respective arguments.

**Availability**:
- macOS ?+

## Declaration

```swift
func getRed(_ red: UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)
```

#### Discussion

If `NULL` is passed in as an argument, the method doesn’t set that value. This method works only with objects representing colors in the [`calibratedRGB`](nscolorspacename/calibratedrgb.md) or [`deviceRGB`](nscolorspacename/devicergb.md) color space. Sending it to other objects raises an exception.

## Parameters

- `red`: Upon return, contains the red component of the color object.
- `green`: Upon return, contains the green component of the color object.
- `blue`: Upon return, contains the blue component of the color object.
- `alpha`: Upon return, contains the opacity value of the color object.

## See Also

- [var blueComponent: CGFloat](nscolor/bluecomponent.md)
  The blue component value of the color.
- [var redComponent: CGFloat](nscolor/redcomponent.md)
  The red component value of the color.
- [var alphaComponent: CGFloat](nscolor/alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var greenComponent: CGFloat](nscolor/greencomponent.md)
  The green component value of the color.
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getcyan(_:magenta:yellow:black:alpha:).md)
  Returns the color object’s CMYK and opacity values.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/gethue(_:saturation:brightness:alpha:).md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getwhite(_:alpha:).md)
  Returns the grayscale and alpha values of the color.
- [var numberOfComponents: Int](nscolor/numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](nscolor/getcomponents(_:).md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/getred(_:green:blue:alpha:))*