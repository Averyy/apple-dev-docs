# screen

**Framework**: AppKit  
**Kind**: property

The bitmapped screen font for the current font.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
var screen: NSFont { get }
```

#### Discussion

For a font object that represents a scalable PostScript font, this property contains a bitmapped screen font matching the receiver in typeface and matrix (or size), or `nil` if such a font cannot be found. For a bitmapped screen font, the value in this property is `nil`.

Screen fonts are for direct use with the window server only. Never use them with Application Kit objects, such as in `setFont:` methods. Internally, the Application Kit automatically uses the corresponding screen font for a font object as long as the view is not rotated or scaled.

## See Also

- [func screenFont(with: NSFontRenderingMode) -> NSFont](nsfont/screenfont(with:).md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
- [var printer: NSFont](nsfont/printer.md)
  The scalable PostScript font corresponding to current font.
- [var renderingMode: NSFontRenderingMode](nsfont/renderingmode.md)
  The rendering mode of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/screen)*