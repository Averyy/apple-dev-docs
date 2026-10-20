# hiraganaToKatakana

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A constant containing the transliteration of a string from Hiragana script to Katakana script.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let hiraganaToKatakana: StringTransform
```

```c
extern NSStringTransform const NSStringTransformHiraganaToKatakana;
```

#### Discussion

This transformation is reversible.

For example, the string “ひらがな” transliterates to “カタカナ”.

This is equivalent to [`kCFStringTransformHiraganaKatakana`](../../CoreFoundation/kcfstringtransformhiraganakatakana.md).

## See Also

### Constants
- [static let latinToKatakana: StringTransform](./latintokatakana.md)
  A constant containing the transliteration of a string from Latin script to Katakana script.
- [static let latinToHiragana: StringTransform](./latintohiragana.md)
  A constant containing the transliteration of a string from Latin script to Hiragana script.
- [static let latinToHangul: StringTransform](./latintohangul.md)
  A constant containing the transliteration of a string from Latin script to Hangul script.
- [static let latinToArabic: StringTransform](./latintoarabic.md)
  A constant containing the transliteration of a string from Latin script to Arabic script.
- [static let latinToHebrew: StringTransform](./latintohebrew.md)
  A constant containing the transliteration of a string from Latin script to Hebrew script.
- [static let latinToThai: StringTransform](./latintothai.md)
  A constant containing the transliteration of a string from Latin script to Thai script.
- [static let latinToCyrillic: StringTransform](./latintocyrillic.md)
  A constant containing the transliteration of a string from Latin script to Cyrillic script.
- [static let toLatin: StringTransform](./tolatin.md)
  A constant containing the transliteration of a string from any script to Latin script.
- [static let mandarinToLatin: StringTransform](./mandarintolatin.md)
  A constant containing the transliteration of a string from Han script to Latin.
- [static let fullwidthToHalfwidth: StringTransform](./fullwidthtohalfwidth.md)
  A constant containing the transformation of a string from full-width CJK characters to half-width forms.
- [static let toXMLHex: StringTransform](./toxmlhex.md)
  A constant containing the transformation of a string from characters to XML hexadecimal escape codes.
- [static let toUnicodeName: StringTransform](./tounicodename.md)
  An identifier for a transform that converts characters to Unicode names.
- [static let stripCombiningMarks: StringTransform](./stripcombiningmarks.md)
  A constant containing the transformation of a string by removing combining marks.
- [static let stripDiacritics: StringTransform](./stripdiacritics.md)
  A constant containing the transformation of a string by removing diacritics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringtransform/hiraganatokatakana)*