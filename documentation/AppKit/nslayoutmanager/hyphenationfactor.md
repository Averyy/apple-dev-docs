# hyphenationFactor

**Framework**: AppKit  
**Kind**: property

The threshold controlling when hyphenation is done.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var hyphenationFactor: Float { get set }
```

#### Discussion

Whenever (width of the real contents of the line) / (the line fragment width) is below `factor`, hyphenation is attempted when laying out the line. Hyphenation slows down text layout and increases memory usage, so it should be used sparingly.

## See Also

- [var usesScreenFonts: Bool](nslayoutmanager/usesscreenfonts.md)
  A Boolean that controls using screen fonts to calculate layout and display text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/hyphenationfactor)*