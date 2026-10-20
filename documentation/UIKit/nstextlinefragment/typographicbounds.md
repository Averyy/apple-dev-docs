# typographicBounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The typographic bounds that specifies the dimensions of the line fragment for laying out line fragments to each other.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var typographicBounds: CGRect { get }
```

```objc
@property (readonly) CGRect typographicBounds;
```

#### Discussion

The origin value is offset from the beginning of the line fragment group belonging to the parent layout fragment.

## See Also

### Line fragment characteristics
- [var attributedString: NSAttributedString](./attributedstring.md)
  The source attributed string.
- [var characterRange: NSRange](./characterrange.md)
  The string range for the source attributed string that corresponds to this line fragment.
- [var glyphOrigin: CGPoint](./glyphorigin.md)
  Rendering origin for the left-most glyph in the line fragment coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/typographicbounds)*