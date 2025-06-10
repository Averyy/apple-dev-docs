# toUnicodeName

**Framework**: Foundation  
**Kind**: property

An identifier for a transform that converts characters to Unicode names.

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
static let toUnicodeName: StringTransform
```

#### Discussion

For example, the string “🐶🐮” transforms to `"``\N{DOG FACE}\N{COW FACE}"` .

Passing this constant to the [`applyTransform(_:reverse:range:updatedRange:)`](nsmutablestring/applytransform(_:reverse:range:updatedrange:).md) method is equivalent to passing [`kCFStringTransformToUnicodeName`](https://developer.apple.com/documentation/CoreFoundation/kCFStringTransformToUnicodeName) to [`CFStringTransform(_:_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFStringTransform(_:_:_:_:)).

> **Note**:  The result of a forward transformation delimits each Unicode name with enclosing curly braces and the leading character sequence `"\N"`. In some programming languages, `"\N{...}"` is used as an escape sequence for Unicode characters in strings and regular expressions; this isn’t supported in Swift or Objective-C. To perform the reverse transform of a string literal in Swift or Objective-C, escape the leading backslash (`"\\N{...}"`) for each Unicode name.

## See Also

- [static let latinToKatakana: StringTransform](stringtransform/latintokatakana.md)
  A constant containing the transliteration of a string from Latin script to Katakana script.
- [static let latinToHiragana: StringTransform](stringtransform/latintohiragana.md)
  A constant containing the transliteration of a string from Latin script to Hiragana script.
- [static let latinToHangul: StringTransform](stringtransform/latintohangul.md)
  A constant containing the transliteration of a string from Latin script to Hangul script.
- [static let latinToArabic: StringTransform](stringtransform/latintoarabic.md)
  A constant containing the transliteration of a string from Latin script to Arabic script.
- [static let latinToHebrew: StringTransform](stringtransform/latintohebrew.md)
  A constant containing the transliteration of a string from Latin script to Hebrew script.
- [static let latinToThai: StringTransform](stringtransform/latintothai.md)
  A constant containing the transliteration of a string from Latin script to Thai script.
- [static let latinToCyrillic: StringTransform](stringtransform/latintocyrillic.md)
  A constant containing the transliteration of a string from Latin script to Cyrillic script.
- [static let toLatin: StringTransform](stringtransform/tolatin.md)
  A constant containing the transliteration of a string from any script to Latin script.
- [static let mandarinToLatin: StringTransform](stringtransform/mandarintolatin.md)
  A constant containing the transliteration of a string from Han script to Latin.
- [static let hiraganaToKatakana: StringTransform](stringtransform/hiraganatokatakana.md)
  A constant containing the transliteration of a string from Hiragana script to Katakana script.
- [static let fullwidthToHalfwidth: StringTransform](stringtransform/fullwidthtohalfwidth.md)
  A constant containing the transformation of a string from full-width CJK characters to half-width forms.
- [static let toXMLHex: StringTransform](stringtransform/toxmlhex.md)
  A constant containing the transformation of a string from characters to XML hexadecimal escape codes.
- [static let stripCombiningMarks: StringTransform](stringtransform/stripcombiningmarks.md)
  A constant containing the transformation of a string by removing combining marks.
- [static let stripDiacritics: StringTransform](stringtransform/stripdiacritics.md)
  A constant containing the transformation of a string by removing diacritics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringtransform/tounicodename)*