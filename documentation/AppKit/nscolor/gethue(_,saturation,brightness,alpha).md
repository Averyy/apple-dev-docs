# getHue(_:saturation:brightness:alpha:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the color object’s HSB component and opacity values in the respective arguments.

**Availability**:
- macOS

## Declaration

```swift
func getHue(_ hue: UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)
```

```objc
- (void) getHue:(CGFloat *) hue saturation:(CGFloat *) saturation brightness:(CGFloat *) brightness alpha:(CGFloat *) alpha;
```

## Discussion

If `NULL` is passed in as an argument, the method doesn’t set that value. This method works only with objects representing colors in the [`calibratedRGB`](../nscolorspacename/calibratedrgb.md) or [`deviceRGB`](../nscolorspacename/devicergb.md) color space. Sending it to other objects raises an exception.

## Parameters

- `hue`: Upon return, contains the hue component of the color object.
- `saturation`: Upon return, contains the saturation component of the color object.
- `brightness`: Upon return, contains the brightness component of the color object.
- `alpha`: Upon return, contains the opacity value of the color object.

## See Also

### Related Documentation
- [var brightnessComponent: CGFloat](./brightnesscomponent.md)
  The brightness component value of the color.
- [var hueComponent: CGFloat](./huecomponent.md)
  The hue component value of the color.
- [var alphaComponent: CGFloat](./alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var saturationComponent: CGFloat](./saturationcomponent.md)
  The saturation component value of the color.
### Retrieving component values from color objects
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getcyan%28_,magenta,yellow,black,alpha%29.md)
  Returns the color object’s CMYK and opacity values.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getred%28_,green,blue,alpha%29.md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getwhite%28_,alpha%29.md)
  Returns the grayscale and alpha values of the color.
- [var numberOfComponents: Int](./numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](./getcomponents%28_%29.md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/gethue(_:saturation:brightness:alpha:))*