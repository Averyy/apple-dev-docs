# hyphenationFactor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The threshold controlling when hyphenation is done.

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

> **Deprecated**: Use [`usesDefaultHyphenation`](./usesdefaulthyphenation.md) instead.

## Declaration

```swift
var hyphenationFactor: Float { get set }
```

```objc
@property float hyphenationFactor;
```

#### Discussion

Whenever (width of the real contents of the line) / (the line fragment width) is below `factor`, hyphenation is attempted when laying out the line. Hyphenation slows down text layout and increases memory usage, so it should be used sparingly.

## See Also

### Deprecated properties
- [var usesScreenFonts: Bool](./usesscreenfonts.md)
  A Boolean that controls using screen fonts to calculate layout and display text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/hyphenationfactor)*