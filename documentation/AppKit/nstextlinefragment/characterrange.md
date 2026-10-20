# characterRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The string range for the source attributed string that corresponds to this line fragment.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var characterRange: NSRange { get }
```

```objc
@property (readonly) NSRange characterRange;
```

## See Also

### Line fragment characteristics
- [var attributedString: NSAttributedString](./attributedstring.md)
  The source attributed string.
- [var glyphOrigin: CGPoint](./glyphorigin.md)
  Rendering origin for the left-most glyph in the line fragment coordinate system.
- [var typographicBounds: CGRect](./typographicbounds.md)
  The typographic bounds that specifies the dimensions of the line fragment for laying out line fragments to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment/characterrange)*