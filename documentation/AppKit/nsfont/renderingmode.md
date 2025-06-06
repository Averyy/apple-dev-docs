# renderingMode

**Framework**: AppKit  
**Kind**: property

The rendering mode of the font.

**Availability**:
- macOS ?+

## Declaration

```swift
var renderingMode: NSFontRenderingMode { get }
```

#### Discussion

For a list of valid rendering modes, see [`NSFontRenderingMode`](nsfontrenderingmode.md).

## See Also

- [func screenFont(with: NSFontRenderingMode) -> NSFont](nsfont/screenfont(with:).md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
- [var printer: NSFont](nsfont/printer.md)
  The scalable PostScript font corresponding to current font.
- [var screen: NSFont](nsfont/screen.md)
  The bitmapped screen font for the current font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/renderingmode)*