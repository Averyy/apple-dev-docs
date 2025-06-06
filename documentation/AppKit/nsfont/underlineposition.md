# underlinePosition

**Framework**: AppKit  
**Kind**: property

The baseline offset to use when drawing underlines with the font.

**Availability**:
- macOS ?+

## Declaration

```swift
var underlinePosition: CGFloat { get }
```

#### Discussion

The value in this property is determined by the font’s AFM file. The value is usually negative, which must be considered when drawing in a flipped coordinate system.

## See Also

- [var italicAngle: CGFloat](nsfont/italicangle.md)
  The number of degrees that the font is slanted counterclockwise from the vertical.
- [var underlineThickness: CGFloat](nsfont/underlinethickness.md)
  The thickness to use when drawing underlines with the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/underlineposition)*