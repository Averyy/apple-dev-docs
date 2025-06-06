# italicAngle

**Framework**: AppKit  
**Kind**: property

The number of degrees that the font is slanted counterclockwise from the vertical.

**Availability**:
- macOS ?+

## Declaration

```swift
var italicAngle: CGFloat { get }
```

#### Discussion

The italic angle value is read from the font’s AFM file. Because the slant is measured counterclockwise, English italic fonts typically return a negative value.

## See Also

- [var underlinePosition: CGFloat](nsfont/underlineposition.md)
  The baseline offset to use when drawing underlines with the font.
- [var underlineThickness: CGFloat](nsfont/underlinethickness.md)
  The thickness to use when drawing underlines with the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/italicangle)*