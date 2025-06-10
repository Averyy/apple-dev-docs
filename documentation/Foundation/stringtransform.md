# StringTransform

**Framework**: Foundation  
**Kind**: struct

Constants representing an ICU string transform.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct StringTransform
```

#### Discussion

These constants are used by the [`NSString`](nsstring.md) method [`applyingTransform(_:reverse:)`](nsstring/applyingtransform(_:reverse:).md).

## Topics

### Transliteration
- [static let toLatin: StringTransform](stringtransform/tolatin.md)
  A constant containing the transliteration of a string from any script to Latin script.
- [static let latinToArabic: StringTransform](stringtransform/latintoarabic.md)
  A constant containing the transliteration of a string from Latin script to Arabic script.
- [static let latinToCyrillic: StringTransform](stringtransform/latintocyrillic.md)
  A constant containing the transliteration of a string from Latin script to Cyrillic script.
- [static let latinToGreek: StringTransform](stringtransform/latintogreek.md)
  A constant containing the transliteration of a string from Latin script to Greek script.
- [static let latinToHangul: StringTransform](stringtransform/latintohangul.md)
  A constant containing the transliteration of a string from Latin script to Hangul script.
- [static let latinToHebrew: StringTransform](stringtransform/latintohebrew.md)
  A constant containing the transliteration of a string from Latin script to Hebrew script.
- [static let latinToHiragana: StringTransform](stringtransform/latintohiragana.md)
  A constant containing the transliteration of a string from Latin script to Hiragana script.
- [static let latinToKatakana: StringTransform](stringtransform/latintokatakana.md)
  A constant containing the transliteration of a string from Latin script to Katakana script.
- [static let latinToThai: StringTransform](stringtransform/latintothai.md)
  A constant containing the transliteration of a string from Latin script to Thai script.
- [static let hiraganaToKatakana: StringTransform](stringtransform/hiraganatokatakana.md)
  A constant containing the transliteration of a string from Hiragana script to Katakana script.
- [static let mandarinToLatin: StringTransform](stringtransform/mandarintolatin.md)
  A constant containing the transliteration of a string from Han script to Latin.
### Diacritic and Combining Mark Removal
- [static let stripDiacritics: StringTransform](stringtransform/stripdiacritics.md)
  A constant containing the transformation of a string by removing diacritics.
- [static let stripCombiningMarks: StringTransform](stringtransform/stripcombiningmarks.md)
  A constant containing the transformation of a string by removing combining marks.
### Halfwidth and Fullwidth Form Conversion
- [static let fullwidthToHalfwidth: StringTransform](stringtransform/fullwidthtohalfwidth.md)
  A constant containing the transformation of a string from full-width CJK characters to half-width forms.
### Character Representation
- [static let toUnicodeName: StringTransform](stringtransform/tounicodename.md)
  An identifier for a transform that converts characters to Unicode names.
- [static let toXMLHex: StringTransform](stringtransform/toxmlhex.md)
  A constant containing the transformation of a string from characters to XML hexadecimal escape codes.
### Initializers
- [init(String)](stringtransform/init(_:).md)
- [init(rawValue: String)](stringtransform/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func applyingTransform(StringTransform, reverse: Bool) -> String?](nsstring/applyingtransform(_:reverse:).md)
  Returns a new string by applying a specified transform to the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringtransform)*