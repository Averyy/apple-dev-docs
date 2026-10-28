# includeLanguageExtents

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

An option to include additional space based on common glyph sequences for various languages.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var includeLanguageExtents: CTLineBoundsOptions { get }
```

```c
kCTLineBoundsIncludeLanguageExtents
```

## Discussion

Use the result of this option when drawing to avoid clipping that the typographic bounds may cause. This option doesn’t have an effect when you use it with [`useGlyphPathBounds`](./useglyphpathbounds.md).

## See Also

### Line Bounds Options
- [static var excludeTypographicLeading: CTLineBoundsOptions](./excludetypographicleading.md)
  An option to exclude typographic leading.
- [static var excludeTypographicShifts: CTLineBoundsOptions](./excludetypographicshifts.md)
  An option to ignore cross-stream shifts due to positioning, such as kerning or baseline alignment.
- [static var useGlyphPathBounds: CTLineBoundsOptions](./useglyphpathbounds.md)
  An option to use glyph path bounds rather than the default typographic bounds.
- [static var useHangingPunctuation: CTLineBoundsOptions](./usehangingpunctuation.md)
  An option to enable hanging punctuation.
- [static var useOpticalBounds: CTLineBoundsOptions](./useopticalbounds.md)
  An option to use optical bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/includelanguageextents)*