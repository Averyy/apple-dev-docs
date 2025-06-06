# descender

**Framework**: AppKit  
**Kind**: property

The bottom y-coordinate, offset from the baseline, of the font’s longest descender.

**Availability**:
- macOS ?+

## Declaration

```swift
var descender: CGFloat { get }
```

#### Discussion

For example, if the longest descender extends 2 points below the baseline, the value in this property is `–2`.

## See Also

- [var ascender: CGFloat](nsfont/ascender.md)
  The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [var capHeight: CGFloat](nsfont/capheight.md)
  The cap height of the font.
- [var leading: CGFloat](nsfont/leading.md)
  The leading value of the font.
- [var xHeight: CGFloat](nsfont/xheight.md)
  The x-height of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/descender)*