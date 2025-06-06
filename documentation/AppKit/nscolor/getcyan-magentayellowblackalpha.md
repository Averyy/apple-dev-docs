# getCyan(_:magenta:yellow:black:alpha:)

**Framework**: AppKit  
**Kind**: method

Returns the color object’s CMYK and opacity values.

**Availability**:
- macOS ?+

## Declaration

```swift
func getCyan(_ cyan: UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)
```

#### Discussion

If `NULL` is passed in as an argument, the method doesn’t set that value. This method works only with objects representing colors in the [`deviceCMYK`](nscolorspacename/devicecmyk.md). Sending it to other objects raises an exception.

## Parameters

- `cyan`: Upon return, contains the cyan component of the color object.
- `magenta`: Upon return, contains the magenta component of the color object.
- `yellow`: Upon return, contains the yellow component of the color object.
- `black`: Upon return, contains the black component of the color object.
- `alpha`: Upon return, contains opacity value of the color object.

## See Also

- [var blackComponent: CGFloat](nscolor/blackcomponent.md)
  The black component value of the color.
- [var cyanComponent: CGFloat](nscolor/cyancomponent.md)
  The cyan component value of the color.
- [var yellowComponent: CGFloat](nscolor/yellowcomponent.md)
  The yellow component value of the color.
- [var magentaComponent: CGFloat](nscolor/magentacomponent.md)
  The magenta component value of the color.
- [var alphaComponent: CGFloat](nscolor/alphacomponent.md)
  The alpha (opacity) component value of the color.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/gethue(_:saturation:brightness:alpha:).md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getred(_:green:blue:alpha:).md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getwhite(_:alpha:).md)
  Returns the grayscale and alpha values of the color.
- [var numberOfComponents: Int](nscolor/numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](nscolor/getcomponents(_:).md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/getcyan(_:magenta:yellow:black:alpha:))*