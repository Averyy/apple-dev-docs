# kCTFontPriorityAttribute

**Framework**: Core Text  
**Kind**: var

The font priority used by font descriptors when resolving duplicates and sorting match results.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTFontPriorityAttribute: CFString
```

#### Discussion

The value associated with this key is an integer represented as a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object containing one of the values enumerated in [`CTFontPriority`](ctfontpriority.md). The higher the value, the higher the priority of the font. Only registered fonts have a priority. Unregistered font descriptors return `NULL`.

## See Also

- [typealias CTFontPriority](ctfontpriority.md)
  The priority of font descriptors when resolving duplicates and sorting match results.
- [let kCTFontURLAttribute: CFString](kctfonturlattribute.md)
  The font URL from the font descriptor.
- [let kCTFontNameAttribute: CFString](kctfontnameattribute.md)
  The PostScript name from the font descriptor.
- [let kCTFontDisplayNameAttribute: CFString](kctfontdisplaynameattribute.md)
  The name used to display the font.
- [let kCTFontFamilyNameAttribute: CFString](kctfontfamilynameattribute.md)
  The font family name from the font descriptor.
- [let kCTFontStyleNameAttribute: CFString](kctfontstylenameattribute.md)
  The style name of the font.
- [let kCTFontTraitsAttribute: CFString](kctfonttraitsattribute.md)
  The dictionary of font traits for stylistic information.
- [let kCTFontVariationAttribute: CFString](kctfontvariationattribute.md)
  The dictionary of font variation.
- [let kCTFontSizeAttribute: CFString](kctfontsizeattribute.md)
  The font point size.
- [let kCTFontMatrixAttribute: CFString](kctfontmatrixattribute.md)
  The font transformation matrix when creating a font.
- [let kCTFontCascadeListAttribute: CFString](kctfontcascadelistattribute.md)
  The cascade list used for a font reference.
- [let kCTFontCharacterSetAttribute: CFString](kctfontcharactersetattribute.md)
  The Unicode character coverage set for a font reference.
- [let kCTFontLanguagesAttribute: CFString](kctfontlanguagesattribute.md)
  A list of covered languages for a font reference.
- [let kCTFontBaselineAdjustAttribute: CFString](kctfontbaselineadjustattribute.md)
  The baseline adjustment for a font reference.
- [let kCTFontMacintoshEncodingsAttribute: CFString](kctfontmacintoshencodingsattribute.md)
  The Macintosh encodings for a font reference.
- [let kCTFontFeaturesAttribute: CFString](kctfontfeaturesattribute.md)
  The font features for a font reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontpriorityattribute)*