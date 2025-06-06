# Transform Identifiers for CFStringTransform

**Framework**: Core Foundation

Constants that identify transforms used with [`CFStringTransform(_:_:_:_:)`](cfstringtransform(_:_:_:_:).md).

#### Overview

In macOS 10.4 and later, with [`CFStringTransform(_:_:_:_:)`](cfstringtransform(_:_:_:_:).md) you can also use any valid ICU transform ID defined in the [`ICU User Guide for Transforms`](https://developer.apple.comhttp://icu.sourceforge.net/userguide/Transform.html).

## Topics

### Constants
- [let kCFStringTransformStripCombiningMarks: CFString!](kcfstringtransformstripcombiningmarks.md)
  The identifier of a transform to strip combining marks (accents or diacritics).
- [let kCFStringTransformToLatin: CFString!](kcfstringtransformtolatin.md)
  The identifier of a transform to transliterate all text possible to Latin script. Ideographs are transliterated as Mandarin Chinese.
- [let kCFStringTransformFullwidthHalfwidth: CFString!](kcfstringtransformfullwidthhalfwidth.md)
  The identifier of a reversible transform to convert full-width characters to their half-width equivalents.
- [let kCFStringTransformLatinKatakana: CFString!](kcfstringtransformlatinkatakana.md)
  The identifier of a reversible transform to transliterate text to Katakana from Latin.
- [let kCFStringTransformLatinHiragana: CFString!](kcfstringtransformlatinhiragana.md)
  The identifier of a reversible transform to transliterate text to Hiragana from Latin.
- [let kCFStringTransformHiraganaKatakana: CFString!](kcfstringtransformhiraganakatakana.md)
  The identifier of a reversible transform to transliterate text to Katakana from Hiragana.
- [let kCFStringTransformMandarinLatin: CFString!](kcfstringtransformmandarinlatin.md)
  The identifier of a transform to transliterate text to Latin from ideographs interpreted as Mandarin Chinese. This transform is not reversible.
- [let kCFStringTransformLatinHangul: CFString!](kcfstringtransformlatinhangul.md)
  The identifier of a reversible transform to transliterate text to Hangul from Latin.
- [let kCFStringTransformLatinArabic: CFString!](kcfstringtransformlatinarabic.md)
  The identifier of a reversible transform to transliterate text to Arabic from Latin.
- [let kCFStringTransformLatinHebrew: CFString!](kcfstringtransformlatinhebrew.md)
  The identifier of a reversible transform to transliterate text to Hebrew from Latin.
- [let kCFStringTransformLatinThai: CFString!](kcfstringtransformlatinthai.md)
  The identifier of a reversible transform to transliterate text to Thai from Latin.
- [let kCFStringTransformLatinCyrillic: CFString!](kcfstringtransformlatincyrillic.md)
  The identifier of a reversible transform to transliterate text to Cyrillic from Latin.
- [let kCFStringTransformLatinGreek: CFString!](kcfstringtransformlatingreek.md)
  The identifier of a reversible transform to transliterate text to Greek from Latin.
- [let kCFStringTransformToXMLHex: CFString!](kcfstringtransformtoxmlhex.md)
  The identifier of a reversible transform to transliterate characters other than printable ASCII to XML/HTML numeric entities.
- [let kCFStringTransformToUnicodeName: CFString!](kcfstringtransformtounicodename.md)
  The identifier of a reversible transform to transliterate characters other than printable ASCII to their Unicode character name in braces.
- [let kCFStringTransformStripDiacritics: CFString!](kcfstringtransformstripdiacritics.md)
  The identifier of a transform to remove diacritic markings.

## See Also

- [enum CFStringNormalizationForm](cfstringnormalizationform.md)
  Unicode normalization forms as described in Unicode Technical Report #15.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/transform-identifiers-for-cfstringtransform)*