# kCTFontFeatureSettingsAttribute

**Framework**: Core Text  
**Kind**: var

The font features settings for a font reference.

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
let kCTFontFeatureSettingsAttribute: CFString
```

#### Discussion

The value associated with this key is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) object containing font feature-setting dictionaries. A feature-setting dictionary contains a tuple of a [`kCTFontFeatureTypeIdentifierKey`](kctfontfeaturetypeidentifierkey.md) key-value pair and a [`kCTFontFeatureSelectorIdentifierKey`](kctfontfeatureselectoridentifierkey.md) key-value pair. Each setting dictionary indicates which setting should be turned on.

> **Note**:  In the case of duplicate or conflicting settings, the last setting in the list takes precedence. It is the caller’s responsibility to handle exclusive and nonexclusive settings as necessary.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontfeaturesettingsattribute)*