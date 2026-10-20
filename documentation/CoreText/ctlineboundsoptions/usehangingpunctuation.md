# useHangingPunctuation

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

An option to enable hanging punctuation.

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
static var useHangingPunctuation: CTLineBoundsOptions { get }
```

```c
kCTLineBoundsUseHangingPunctuation
```

#### Discussion

The result of this option moves standard punctuation, such as periods, commas, hyphens, dashes, quotation marks, and asterisks, into the margin of either end of text, to give the appearance of a more uniform vertical alignment. Consider using this option when the text is fully justified.

## See Also

### Line Bounds Options
- [static var excludeTypographicLeading: CTLineBoundsOptions](./excludetypographicleading.md)
  An option to exclude typographic leading.
- [static var excludeTypographicShifts: CTLineBoundsOptions](./excludetypographicshifts.md)
  An option to ignore cross-stream shifts due to positioning, such as kerning or baseline alignment.
- [static var includeLanguageExtents: CTLineBoundsOptions](./includelanguageextents.md)
  An option to include additional space based on common glyph sequences for various languages.
- [static var useGlyphPathBounds: CTLineBoundsOptions](./useglyphpathbounds.md)
  An option to use glyph path bounds rather than the default typographic bounds.
- [static var useOpticalBounds: CTLineBoundsOptions](./useopticalbounds.md)
  An option to use optical bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/usehangingpunctuation)*