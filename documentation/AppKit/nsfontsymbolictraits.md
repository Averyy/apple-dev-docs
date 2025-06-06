# NSFontSymbolicTraits

**Framework**: AppKit  
**Kind**: typealias

A symbolic description of stylistic aspects of a font.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias NSFontSymbolicTraits = UInt32
```

#### Discussion

The upper 16 bits is used to describe appearance of the font (see [`NSFontFamilyClass`](nsfontfamilyclass.md)) whereas the lower 16 bits is used for typeface information (see [`Typeface Information`](typeface-information.md)). The font appearance information represented by the upper 16 bits can be used for stylistic font matching. The symbolic traits supersede the existing [`NSFontTraitMask`](nsfonttraitmask.md) type used by [`NSFontManager`](nsfontmanager.md). The corresponding values are kept compatible between [`NSFontTraitMask`](nsfonttraitmask.md) and [`NSFontSymbolicTraits`](nsfontsymbolictraits.md).

## See Also

- [class NSFont](nsfont.md)
  The representation of a font in an app.
- [class NSFontDescriptor](nsfontdescriptor.md)
  A dictionary of attributes that describe a font.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [class NSFontAssetRequest](nsfontassetrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontsymbolictraits)*