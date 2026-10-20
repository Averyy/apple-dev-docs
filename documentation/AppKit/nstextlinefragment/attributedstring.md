# attributedString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The source attributed string.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var attributedString: NSAttributedString { get }
```

```objc
@property (strong, readonly) NSAttributedString * attributedString;
```

## See Also

### Line fragment characteristics
- [var characterRange: NSRange](./characterrange.md)
  The string range for the source attributed string that corresponds to this line fragment.
- [var glyphOrigin: CGPoint](./glyphorigin.md)
  Rendering origin for the left-most glyph in the line fragment coordinate system.
- [var typographicBounds: CGRect](./typographicbounds.md)
  The typographic bounds that specifies the dimensions of the line fragment for laying out line fragments to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment/attributedstring)*