# underlinePosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The baseline offset to use when drawing underlines with the font.

**Availability**:
- macOS

## Declaration

```swift
var underlinePosition: CGFloat { get }
```

```objc
@property (readonly) CGFloat underlinePosition;
```

## Discussion

The value in this property is determined by the font’s AFM file. The value is usually negative, which must be considered when drawing in a flipped coordinate system.

## See Also

### Getting Underline and Italic Metrics
- [var italicAngle: CGFloat](./italicangle.md)
  The number of degrees that the font is slanted counterclockwise from the vertical.
- [var underlineThickness: CGFloat](./underlinethickness.md)
  The thickness to use when drawing underlines with the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/underlineposition)*