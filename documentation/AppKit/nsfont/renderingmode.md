# renderingMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rendering mode of the font.

**Availability**:
- macOS

## Declaration

```swift
var renderingMode: NSFontRenderingMode { get }
```

```objc
@property (readonly) NSFontRenderingMode renderingMode;
```

## Discussion

For a list of valid rendering modes, see [`NSFontRenderingMode`](../nsfontrenderingmode.md).

## See Also

### Related Documentation
- [func screenFont(with: NSFontRenderingMode) -> NSFont](./screenfont%28with%29.md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
### Instance Properties
- [var printer: NSFont](./printer.md)
  The scalable PostScript font corresponding to current font.
- [var screen: NSFont](./screen.md)
  The bitmapped screen font for the current font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/renderingmode)*