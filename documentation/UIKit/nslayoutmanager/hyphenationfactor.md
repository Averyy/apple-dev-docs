# hyphenationFactor

**Framework**: UIKit  
**Kind**: property

The threshold controlling when hyphenation is done.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- tvOS 9.0+

## Declaration

```swift
var hyphenationFactor: CGFloat { get set }
```

#### Discussion

Whenever (width of the real contents of the line) / (the line fragment width) is below `factor`, hyphenation is attempted when laying out the line. Hyphenation slows down text layout and increases memory usage, so it should be used sparingly.

## See Also

- [attributedString](nslayoutmanager-attributedstring.md)
  The text storage object from which the `NSGlyphGenerator` object procures characters for glyph generation.
- [layoutOptions](nslayoutmanager-layoutoptions.md)
  The layout manager’s current layout options.
- [var usesScreenFonts: Bool { get set }](../AppKit/NSLayoutManager/usesScreenFonts.md)
  A Boolean that controls using screen fonts to calculate layout and display text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/hyphenationfactor)*