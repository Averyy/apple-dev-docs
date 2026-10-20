# getWhite(_:alpha:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the grayscale and alpha values of the color.

**Availability**:
- macOS

## Declaration

```swift
func getWhite(_ white: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)
```

```objc
- (void) getWhite:(CGFloat *) white alpha:(CGFloat *) alpha;
```

#### Discussion

If `NULL` is passed in as an argument, the method doesn’t set that value. This method works only with objects representing colors in the [`calibratedWhite`](../nscolorspacename/calibratedwhite.md), [`NSCalibratedBlackColorSpace`](../nscalibratedblackcolorspace.md), [`NSDeviceBlackColorSpace`](../nsdeviceblackcolorspace.md), or [`deviceWhite`](../nscolorspacename/devicewhite.md) color space. Sending it to other objects raises an exception.

## Parameters

- `white`: Upon return, contains the grayscale value of the color object.
- `alpha`: Upon return, contains the opacity value of the color object.

## See Also

### Related Documentation
- [class NSColor](../nscolor.md)
  An object that stores color data and sometimes opacity (alpha value).
### Retrieving component values from color objects
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getcyan%28_,magenta,yellow,black,alpha%29.md)
  Returns the color object’s CMYK and opacity values.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./gethue%28_,saturation,brightness,alpha%29.md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getred%28_,green,blue,alpha%29.md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [var numberOfComponents: Int](./numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](./getcomponents%28_%29.md)
  Returns the components of the color as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/getwhite(_:alpha:))*