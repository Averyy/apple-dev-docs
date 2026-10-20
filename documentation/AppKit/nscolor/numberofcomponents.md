# numberOfComponents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of components in the color.

**Availability**:
- macOS

## Declaration

```swift
var numberOfComponents: Int { get }
```

```objc
@property (readonly) NSInteger numberOfComponents;
```

#### Discussion

This property reflects the number of floating-point component values in the color and includes the alpha component. If the color object does not have any floating-point component values, accessing this property raises an exception.

## See Also

### Related Documentation
- [var colorSpace: NSColorSpace](./colorspace.md)
  The color space associated with the color.
### Retrieving component values from color objects
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getcyan%28_,magenta,yellow,black,alpha%29.md)
  Returns the color object’s CMYK and opacity values.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./gethue%28_,saturation,brightness,alpha%29.md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getred%28_,green,blue,alpha%29.md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getwhite%28_,alpha%29.md)
  Returns the grayscale and alpha values of the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](./getcomponents%28_%29.md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/numberofcomponents)*