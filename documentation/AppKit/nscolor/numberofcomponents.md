# numberOfComponents

**Framework**: AppKit  
**Kind**: property

The number of components in the color.

**Availability**:
- macOS ?+

## Declaration

```swift
var numberOfComponents: Int { get }
```

#### Discussion

This property reflects the number of floating-point component values in the color and includes the alpha component. If the color object does not have any floating-point component values, accessing this property raises an exception.

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
- [func getComponents(UnsafeMutablePointer<CGFloat>)](nscolor/getcomponents(_:).md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/numberofcomponents)*