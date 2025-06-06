# availableFontNames(with:)

**Framework**: AppKit  
**Kind**: method

Returns the names of the fonts available in the system whose traits are described exactly by the given font trait mask (not the `NSFont` objects themselves).

**Availability**:
- macOS ?+

## Declaration

```swift
func availableFontNames(with someTraits: NSFontTraitMask) -> [String]?
```

#### Return Value

The names of the corresponding fonts.

#### Discussion

These fonts are in various system font directories.

If `someTraits` is 0, this method returns all fonts that are neither italic nor bold. This result is the same one you’d get if `fontTraitMask` were `NSUnitalicFontMask` `|` `NSUnboldFontMask`.

## Parameters

- `someTraits`: The font traits for which to return font names. You specify the desired traits by combining the font trait mask values described in   using the C bitwise OR operator.

## See Also

- [var availableFonts: [String]](nsfontmanager/availablefonts.md)
  The names of the fonts available in the system (not the [`NSFont`](nsfont.md) objects themselves).
- [var availableFontFamilies: [String]](nsfontmanager/availablefontfamilies.md)
  The names of the font families available in the system.
- [func availableMembers(ofFontFamily: String) -> [[Any]]?](nsfontmanager/availablemembers(offontfamily:).md)
  Returns an array with one entry for each available member of a font family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/availablefontnames(with:))*