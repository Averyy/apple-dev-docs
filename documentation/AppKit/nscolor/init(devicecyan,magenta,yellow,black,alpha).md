# init(deviceCyan:magenta:yellow:black:alpha:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the given opacity value and CMYK components.

**Availability**:
- macOS

## Declaration

```swift
init(deviceCyan cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)
```

```objc
+ (NSColor *) colorWithDeviceCyan:(CGFloat) cyan magenta:(CGFloat) magenta yellow:(CGFloat) yellow black:(CGFloat) black alpha:(CGFloat) alpha;
```

#### Return Value

The color object.

#### Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Parameters

- `cyan`: The cyan component of the color object.
- `magenta`: The magenta component of the color object.
- `yellow`: The yellow component of the color object.
- `black`: The black component of the color object.
- `alpha`: The opacity value of the color object.

## See Also

### Related Documentation
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getcyan%28_,magenta,yellow,black,alpha%29.md)
  Returns the color object’s CMYK and opacity values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(devicecyan:magenta:yellow:black:alpha:))*