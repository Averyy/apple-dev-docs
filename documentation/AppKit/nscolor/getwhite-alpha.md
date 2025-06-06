# getWhite(_:alpha:)

**Framework**: AppKit  
**Kind**: method

Returns the grayscale and alpha values of the color.

**Availability**:
- macOS ?+

## Declaration

```swift
func getWhite(_ white: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)
```

#### Discussion

If `NULL` is passed in as an argument, the method doesn’t set that value. This method works only with objects representing colors in the [`calibratedWhite`](nscolorspacename/calibratedwhite.md), [`NSCalibratedBlackColorSpace`](nscalibratedblackcolorspace.md), [`NSDeviceBlackColorSpace`](nsdeviceblackcolorspace.md), or [`deviceWhite`](nscolorspacename/devicewhite.md) color space. Sending it to other objects raises an exception.

## Parameters

- `white`: Upon return, contains the grayscale value of the color object.
- `alpha`: Upon return, contains the opacity value of the color object.

## See Also

- [class NSColor](nscolor.md)
  An object that stores color data and sometimes opacity (alpha value).
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getcyan(_:magenta:yellow:black:alpha:).md)
  Returns the color object’s CMYK and opacity values.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/gethue(_:saturation:brightness:alpha:).md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getred(_:green:blue:alpha:).md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [var numberOfComponents: Int](nscolor/numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](nscolor/getcomponents(_:).md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/getwhite(_:alpha:))*