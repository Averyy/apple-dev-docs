# getComponents(_:)

**Framework**: AppKit  
**Kind**: method

Returns the components of the color as an array.

**Availability**:
- macOS ?+

## Declaration

```swift
func getComponents(_ components: UnsafeMutablePointer<CGFloat>)
```

#### Discussion

You can invoke this method on `NSColor` objects created from custom color spaces to get the individual floating-point components, including alpha. Raises an exception if the receiver doesn’t have floating-point components. To find out how many components are in the `components` array, use the [`numberOfComponents`](nscolor/numberofcomponents.md) property.

## Parameters

- `components`: An array containing the components of the color object as   values.

## See Also

- [var colorSpace: NSColorSpace](nscolor/colorspace.md)
  The color space associated with the color.
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getcyan(_:magenta:yellow:black:alpha:).md)
  Returns the color object’s CMYK and opacity values.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/gethue(_:saturation:brightness:alpha:).md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getred(_:green:blue:alpha:).md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getwhite(_:alpha:).md)
  Returns the grayscale and alpha values of the color.
- [var numberOfComponents: Int](nscolor/numberofcomponents.md)
  The number of components in the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/getcomponents(_:))*