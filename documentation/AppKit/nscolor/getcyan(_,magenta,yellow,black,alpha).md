# getCyan(_:magenta:yellow:black:alpha:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the color object’s CMYK and opacity values.

**Availability**:
- macOS

## Declaration

```swift
func getCyan(_ cyan: UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)
```

```objc
- (void) getCyan:(CGFloat *) cyan magenta:(CGFloat *) magenta yellow:(CGFloat *) yellow black:(CGFloat *) black alpha:(CGFloat *) alpha;
```

#### Discussion

If `NULL` is passed in as an argument, the method doesn’t set that value. This method works only with objects representing colors in the [`deviceCMYK`](../nscolorspacename/devicecmyk.md). Sending it to other objects raises an exception.

## Parameters

- `cyan`: Upon return, contains the cyan component of the color object.
- `magenta`: Upon return, contains the magenta component of the color object.
- `yellow`: Upon return, contains the yellow component of the color object.
- `black`: Upon return, contains the black component of the color object.
- `alpha`: Upon return, contains opacity value of the color object.

## See Also

### Related Documentation
- [var blackComponent: CGFloat](./blackcomponent.md)
  The black component value of the color.
- [var cyanComponent: CGFloat](./cyancomponent.md)
  The cyan component value of the color.
- [var yellowComponent: CGFloat](./yellowcomponent.md)
  The yellow component value of the color.
- [var magentaComponent: CGFloat](./magentacomponent.md)
  The magenta component value of the color.
- [var alphaComponent: CGFloat](./alphacomponent.md)
  The alpha (opacity) component value of the color.
### Retrieving component values from color objects
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./gethue%28_,saturation,brightness,alpha%29.md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getred%28_,green,blue,alpha%29.md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getwhite%28_,alpha%29.md)
  Returns the grayscale and alpha values of the color.
- [var numberOfComponents: Int](./numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](./getcomponents%28_%29.md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/getcyan(_:magenta:yellow:black:alpha:))*