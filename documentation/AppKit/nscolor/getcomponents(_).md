# getComponents(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the components of the color as an array.

**Availability**:
- macOS

## Declaration

```swift
func getComponents(_ components: UnsafeMutablePointer<CGFloat>)
```

```objc
- (void) getComponents:(CGFloat *) components;
```

#### Discussion

You can invoke this method on `NSColor` objects created from custom color spaces to get the individual floating-point components, including alpha. Raises an exception if the receiver doesn’t have floating-point components. To find out how many components are in the `components` array, use the [`numberOfComponents`](./numberofcomponents.md) property.

## Parameters

- `components`: An array containing the components of the color object as `float` values.

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
- [var numberOfComponents: Int](./numberofcomponents.md)
  The number of components in the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/getcomponents(_:))*