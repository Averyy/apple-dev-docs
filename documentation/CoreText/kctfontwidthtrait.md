# kCTFontWidthTrait

**Framework**: Core Text  
**Kind**: var

The normalized proportion (width condense or expand) trait from the font traits dictionary.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTFontWidthTrait: CFString
```

#### Discussion

This value corresponds to the relative interglyph spacing for a given font. The value returned is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object representing a float between `-1.0` and `1.0`. The value of `0.0` corresponds to regular glyph spacing, and negative values represent condensed glyph spacing.

## See Also

- [let kCTFontSymbolicTrait: CFString](kctfontsymbolictrait.md)
  The symbolic traits value from the font traits dictionary.
- [let kCTFontWeightTrait: CFString](kctfontweighttrait.md)
  The normalized weight trait from the font traits dictionary.
- [let kCTFontSlantTrait: CFString](kctfontslanttrait.md)
  The normalized slant angle from the font traits dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontwidthtrait)*