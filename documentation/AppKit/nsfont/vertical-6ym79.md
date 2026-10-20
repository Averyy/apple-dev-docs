# vertical

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A vertical version of the font.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
var vertical: NSFont { get }
```

```objc
@property (copy, readonly) NSFont * verticalFont;
```

#### Discussion

The value in this property is a vertical version of the font, if such a configuration is supported. If a vertical configuration is not supported, the value in the property is `self`.

A vertical font applies appropriate rotation to the text matrix in [`set(in:)`](./set%28in%29.md), returns vertical metrics, and enables the vertical glyph substitution feature by default.

## See Also

### Vertical Fonts
- [var isVertical: Bool](./isvertical.md)
  A Boolean value indicating whether the font is a vertical font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/vertical-6ym79)*