# latinToGreek

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A constant containing the transliteration of a string from Latin script to Greek script.

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
static let latinToGreek: StringTransform
```

```c
extern NSStringTransform const NSStringTransformLatinToGreek;
```

## Discussion

This transformation is reversible.

For example, the string “Ellēnikó alphábēto‎” transliterates to “Ελληνικό αλφάβητο”.

This is equivalent to [`kCFStringTransformLatinGreek`](../../CoreFoundation/kcfstringtransformlatingreek.md).

## See Also

### Transliteration
- [static let toLatin: StringTransform](./tolatin.md)
  A constant containing the transliteration of a string from any script to Latin script.
- [static let latinToArabic: StringTransform](./latintoarabic.md)
  A constant containing the transliteration of a string from Latin script to Arabic script.
- [static let latinToCyrillic: StringTransform](./latintocyrillic.md)
  A constant containing the transliteration of a string from Latin script to Cyrillic script.
- [static let latinToHangul: StringTransform](./latintohangul.md)
  A constant containing the transliteration of a string from Latin script to Hangul script.
- [static let latinToHebrew: StringTransform](./latintohebrew.md)
  A constant containing the transliteration of a string from Latin script to Hebrew script.
- [static let latinToHiragana: StringTransform](./latintohiragana.md)
  A constant containing the transliteration of a string from Latin script to Hiragana script.
- [static let latinToKatakana: StringTransform](./latintokatakana.md)
  A constant containing the transliteration of a string from Latin script to Katakana script.
- [static let latinToThai: StringTransform](./latintothai.md)
  A constant containing the transliteration of a string from Latin script to Thai script.
- [static let hiraganaToKatakana: StringTransform](./hiraganatokatakana.md)
  A constant containing the transliteration of a string from Hiragana script to Katakana script.
- [static let mandarinToLatin: StringTransform](./mandarintolatin.md)
  A constant containing the transliteration of a string from Han script to Latin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringtransform/latintogreek)*