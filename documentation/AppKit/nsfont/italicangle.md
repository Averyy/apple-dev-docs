# italicAngle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of degrees that the font is slanted counterclockwise from the vertical.

**Availability**:
- macOS

## Declaration

```swift
var italicAngle: CGFloat { get }
```

```objc
@property (readonly) CGFloat italicAngle;
```

## Discussion

The italic angle value is read from the font’s AFM file. Because the slant is measured counterclockwise, English italic fonts typically return a negative value.

## See Also

### Getting Underline and Italic Metrics
- [var underlinePosition: CGFloat](./underlineposition.md)
  The baseline offset to use when drawing underlines with the font.
- [var underlineThickness: CGFloat](./underlinethickness.md)
  The thickness to use when drawing underlines with the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/italicangle)*