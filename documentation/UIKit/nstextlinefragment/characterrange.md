# characterRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The string range for the source attributed string that corresponds to this line fragment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/characterrange)*