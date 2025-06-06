# convertWeight(_:of:)

**Framework**: AppKit  
**Kind**: method

Returns a font object whose weight is greater or lesser than that of the given font.

**Availability**:
- macOS ?+

## Declaration

```swift
func convertWeight(_ upFlag: Bool, of fontObj: NSFont) -> NSFont
```

#### Return Value

A font with matching traits except for the new weight, or `aFont` if it can’t be converted.

#### Discussion

Weights are graded along the following scale. The list on the left gives Apple’s terminology, and the list on the right gives the ISO equivalents. Names on the same line are treated as identical:

| Apple Terminology | ISO Equivalent |
| --- | --- |
| 1. ultralight |  |
| 2. thin | W1. ultralight |
| 3. light, extralight | W2. extralight |
| 4. book | W3. light |
| 5. regular, plain, display, roman | W4. semilight |
| 6. medium | W5. medium |
| 7. demi, demibold |  |
| 8. semi, semibold | W6. semibold |
| 9. bold | W7. bold |
| 10. extra, extrabold | W8. extrabold |
| 11. heavy, heavyface |  |
| 12. black, super | W9. ultrabold |
| 13. ultra, ultrablack, fat |  |
| 14. extrablack, obese, nord |  |

The `NSFontManager` implementation of this method refuses to convert a font’s weight if it can’t maintain all other traits, such as italic and condensed. You might wish to override this method to allow a looser interpretation of weight conversion.

## Parameters

- `upFlag`: If  , a heavier font is returned; if it’s  , a lighter font is returned.
- `fontObj`: The font whose weight is increased or decreased.

## See Also

- [func convert(NSFont) -> NSFont](nsfontmanager/convert(_:).md)
  Converts the given font according to the object that initiated a font change, typically the Font panel or Font menu.
- [func convert(NSFont, toFace: String) -> NSFont?](nsfontmanager/convert(_:toface:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.
- [func convert(NSFont, toFamily: String) -> NSFont](nsfontmanager/convert(_:tofamily:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [func convert(NSFont, toHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tohavetrait:).md)
  Returns a new version of the font object containing a single additional trait.
- [func convert(NSFont, toNotHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tonothavetrait:).md)
  Returns a new version of a font object without the specified traits.
- [func convert(NSFont, toSize: CGFloat) -> NSFont](nsfontmanager/convert(_:tosize:).md)
  Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [var currentFontAction: NSFontAction](nsfontmanager/currentfontaction.md)
  The current font conversion action.
- [func convertFontTraits(NSFontTraitMask) -> NSFontTraitMask](nsfontmanager/convertfonttraits(_:).md)
  Converts font traits to a new traits mask value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/convertweight(_:of:))*