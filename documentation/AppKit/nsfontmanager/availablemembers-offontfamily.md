# availableMembers(ofFontFamily:)

**Framework**: AppKit  
**Kind**: method

Returns an array with one entry for each available member of a font family.

**Availability**:
- macOS ?+

## Declaration

```swift
func availableMembers(ofFontFamily fam: String) -> [[Any]]?
```

#### Return Value

The available members of `family`. See the following discussion for a specific description.

#### Discussion

Each entry of the returned `NSArray` is another `NSArray` with four members, as follows:

- 1. The PostScript font name, as an `NSString` object.
- 1. The part of the font name used in the font panel that’s not the font name, as an `NSString` object. This value is not localized—for example, `"Roman"`, `"Italic"`, or `"Bold"`.
- 1. The font’s weight, as an `NSNumber`.
- 1. The font’s traits, as an `NSNumber`.

The members of the family are arranged in the font panel order (narrowest to widest, lightest to boldest, plain to italic).

For example, if you call `availableMembersOfFontFamily:@"Times"`, it might return an array like this:

```objc
(("Times-Roman", "Roman", 5, 4),
 ("Times-Italic", "Italic", 6, 5),
 ("Times-Bold", "Bold", 9, 2),
 ("Times-BoldItalic", "Bold Italic", 9, 3)
)
```

## Parameters

- `fam`: The name of a font family, like one specified by the value of  .

## See Also

- [var availableFonts: [String]](nsfontmanager/availablefonts.md)
  The names of the fonts available in the system (not the [`NSFont`](nsfont.md) objects themselves).
- [var availableFontFamilies: [String]](nsfontmanager/availablefontfamilies.md)
  The names of the font families available in the system.
- [func availableFontNames(with: NSFontTraitMask) -> [String]?](nsfontmanager/availablefontnames(with:).md)
  Returns the names of the fonts available in the system whose traits are described exactly by the given font trait mask (not the `NSFont` objects themselves).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/availablemembers(offontfamily:))*