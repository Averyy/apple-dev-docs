# printer

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scalable PostScript font corresponding to current font.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var printer: NSFont { get }
```

```objc
@property (copy, readonly) NSFont * printerFont;
```

## Discussion

For a font that already represents a scalable PostScript font, the value in this property is `self`. For a bitmapped screen font, the value is the corresponding scalable PostScript font.

## See Also

### Instance Properties
- [var renderingMode: NSFontRenderingMode](./renderingmode.md)
  The rendering mode of the font.
- [var screen: NSFont](./screen.md)
  The bitmapped screen font for the current font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/printer)*