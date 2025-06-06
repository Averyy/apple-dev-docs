# isGraphemeBase

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the scalar is a grapheme base.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isGraphemeBase: Bool { get }
```

#### Discussion

A grapheme base can be thought of as a space-occupying glyph above or below which other non-spacing modifying glyphs can be applied. For example, when the character `é` is represented in its decomposed form, the grapheme base is “e” (U+0065 LATIN SMALL LETTER E) and it is followed by a single grapheme extender, U+0301 COMBINING ACUTE ACCENT.

The set of scalars for which `isGraphemeBase` is `true` is disjoint by definition from the set for which `isGraphemeExtend` is `true`.

This property corresponds to the “Grapheme_Base” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isgraphemebase)*