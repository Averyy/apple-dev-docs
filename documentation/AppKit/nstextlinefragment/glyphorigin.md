# glyphOrigin

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Rendering origin for the left-most glyph in the line fragment coordinate system.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var glyphOrigin: CGPoint { get }
```

```objc
@property (readonly) CGPoint glyphOrigin;
```

## See Also

### Line fragment characteristics
- [var attributedString: NSAttributedString](./attributedstring.md)
  The source attributed string.
- [var characterRange: NSRange](./characterrange.md)
  The string range for the source attributed string that corresponds to this line fragment.
- [var typographicBounds: CGRect](./typographicbounds.md)
  The typographic bounds that specifies the dimensions of the line fragment for laying out line fragments to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment/glyphorigin)*