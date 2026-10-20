# Locale.LanguageCode

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

An alphabetical code associated with a language.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct LanguageCode
```

## Topics

### Creating a language code
- [init(String)](./languagecode-swift.struct/init%28_%29.md)
  Creates a language code from an identifier.
- [init(stringLiteral: String)](./languagecode-swift.struct/init%28stringliteral%29.md)
  Creates a language code from an identifier as a string literal.
### Examining language code properties
- [var identifier: String](./languagecode-swift.struct/identifier.md)
  The identifier used to create the language code.
- [var isISOLanguage: Bool](./languagecode-swift.struct/isisolanguage.md)
  A Boolean value that indicates whether this language code is in the list of ISO-defined languages.
### Using ISO-defined language codes
- [static var isoLanguageCodes: [Locale.LanguageCode]](./languagecode-swift.struct/isolanguagecodes.md)
  Returns an array of ISO-defined language codes.
### Instance Methods
- [func identifier(Locale.LanguageCode.IdentifierType) -> String?](./languagecode-swift.struct/identifier%28_%29.md)
  Returns the ISO code of the given identifier type. Returns nil if the language isn’t a valid ISO language, or if the specified identifier type isn’t available to the language.
### Type Properties
- [static var ainu: Locale.LanguageCode](./languagecode-swift.struct/ainu.md)
- [static var albanian: Locale.LanguageCode](./languagecode-swift.struct/albanian.md)
- [static var amharic: Locale.LanguageCode](./languagecode-swift.struct/amharic.md)
- [static var apacheWestern: Locale.LanguageCode](./languagecode-swift.struct/apachewestern.md)
- [static var arabic: Locale.LanguageCode](./languagecode-swift.struct/arabic.md)
- [static var armenian: Locale.LanguageCode](./languagecode-swift.struct/armenian.md)
- [static var assamese: Locale.LanguageCode](./languagecode-swift.struct/assamese.md)
- [static var assyrian: Locale.LanguageCode](./languagecode-swift.struct/assyrian.md)
- [static var azerbaijani: Locale.LanguageCode](./languagecode-swift.struct/azerbaijani.md)
- [static var bangla: Locale.LanguageCode](./languagecode-swift.struct/bangla.md)
- [static var belarusian: Locale.LanguageCode](./languagecode-swift.struct/belarusian.md)
- [static var bodo: Locale.LanguageCode](./languagecode-swift.struct/bodo.md)
- [static var bulgarian: Locale.LanguageCode](./languagecode-swift.struct/bulgarian.md)
- [static var burmese: Locale.LanguageCode](./languagecode-swift.struct/burmese.md)
- [static var cantonese: Locale.LanguageCode](./languagecode-swift.struct/cantonese.md)
- [static var catalan: Locale.LanguageCode](./languagecode-swift.struct/catalan.md)
- [static var cherokee: Locale.LanguageCode](./languagecode-swift.struct/cherokee.md)
- [static var chinese: Locale.LanguageCode](./languagecode-swift.struct/chinese.md)
- [static var croatian: Locale.LanguageCode](./languagecode-swift.struct/croatian.md)
- [static var czech: Locale.LanguageCode](./languagecode-swift.struct/czech.md)
- [static var danish: Locale.LanguageCode](./languagecode-swift.struct/danish.md)
- [static var dhivehi: Locale.LanguageCode](./languagecode-swift.struct/dhivehi.md)
- [static var dogri: Locale.LanguageCode](./languagecode-swift.struct/dogri.md)
- [static var dutch: Locale.LanguageCode](./languagecode-swift.struct/dutch.md)
- [static var dzongkha: Locale.LanguageCode](./languagecode-swift.struct/dzongkha.md)
- [static var english: Locale.LanguageCode](./languagecode-swift.struct/english.md)
- [static var estonian: Locale.LanguageCode](./languagecode-swift.struct/estonian.md)
- [static var faroese: Locale.LanguageCode](./languagecode-swift.struct/faroese.md)
- [static var finnish: Locale.LanguageCode](./languagecode-swift.struct/finnish.md)
- [static var french: Locale.LanguageCode](./languagecode-swift.struct/french.md)
- [static var fula: Locale.LanguageCode](./languagecode-swift.struct/fula.md)
- [static var georgian: Locale.LanguageCode](./languagecode-swift.struct/georgian.md)
- [static var german: Locale.LanguageCode](./languagecode-swift.struct/german.md)
- [static var greek: Locale.LanguageCode](./languagecode-swift.struct/greek.md)
- [static var gujarati: Locale.LanguageCode](./languagecode-swift.struct/gujarati.md)
- [static var hawaiian: Locale.LanguageCode](./languagecode-swift.struct/hawaiian.md)
- [static var hebrew: Locale.LanguageCode](./languagecode-swift.struct/hebrew.md)
- [static var hindi: Locale.LanguageCode](./languagecode-swift.struct/hindi.md)
- [static var hungarian: Locale.LanguageCode](./languagecode-swift.struct/hungarian.md)
- [static var icelandic: Locale.LanguageCode](./languagecode-swift.struct/icelandic.md)
- [static var igbo: Locale.LanguageCode](./languagecode-swift.struct/igbo.md)
- [static var indonesian: Locale.LanguageCode](./languagecode-swift.struct/indonesian.md)
- [static var irish: Locale.LanguageCode](./languagecode-swift.struct/irish.md)
- [static var italian: Locale.LanguageCode](./languagecode-swift.struct/italian.md)
- [static var japanese: Locale.LanguageCode](./languagecode-swift.struct/japanese.md)
- [static var kannada: Locale.LanguageCode](./languagecode-swift.struct/kannada.md)
- [static var kashmiri: Locale.LanguageCode](./languagecode-swift.struct/kashmiri.md)
- [static var kazakh: Locale.LanguageCode](./languagecode-swift.struct/kazakh.md)
- [static var khmer: Locale.LanguageCode](./languagecode-swift.struct/khmer.md)
- [static var konkani: Locale.LanguageCode](./languagecode-swift.struct/konkani.md)
- [static var korean: Locale.LanguageCode](./languagecode-swift.struct/korean.md)
- [static var kurdish: Locale.LanguageCode](./languagecode-swift.struct/kurdish.md)
- [static var kurdishSorani: Locale.LanguageCode](./languagecode-swift.struct/kurdishsorani.md)
- [static var kyrgyz: Locale.LanguageCode](./languagecode-swift.struct/kyrgyz.md)
- [static var lao: Locale.LanguageCode](./languagecode-swift.struct/lao.md)
- [static var latvian: Locale.LanguageCode](./languagecode-swift.struct/latvian.md)
- [static var lithuanian: Locale.LanguageCode](./languagecode-swift.struct/lithuanian.md)
- [static var māori: Locale.LanguageCode](./languagecode-swift.struct/m_ori.md)
- [static var macedonian: Locale.LanguageCode](./languagecode-swift.struct/macedonian.md)
- [static var maithili: Locale.LanguageCode](./languagecode-swift.struct/maithili.md)
- [static var malay: Locale.LanguageCode](./languagecode-swift.struct/malay.md)
- [static var malayalam: Locale.LanguageCode](./languagecode-swift.struct/malayalam.md)
- [static var maltese: Locale.LanguageCode](./languagecode-swift.struct/maltese.md)
- [static var manipuri: Locale.LanguageCode](./languagecode-swift.struct/manipuri.md)
- [static var marathi: Locale.LanguageCode](./languagecode-swift.struct/marathi.md)
- [static var mongolian: Locale.LanguageCode](./languagecode-swift.struct/mongolian.md)
- [static let multiple: Locale.LanguageCode](./languagecode-swift.struct/multiple.md)
  The `mul` code: represents the language of some content when there are more than one languages
- [static var navajo: Locale.LanguageCode](./languagecode-swift.struct/navajo.md)
- [static var nepali: Locale.LanguageCode](./languagecode-swift.struct/nepali.md)
- [static var norwegian: Locale.LanguageCode](./languagecode-swift.struct/norwegian.md)
- [static var norwegianBokmål: Locale.LanguageCode](./languagecode-swift.struct/norwegianbokm_l.md)
- [static var norwegianNynorsk: Locale.LanguageCode](./languagecode-swift.struct/norwegiannynorsk.md)
- [static var odia: Locale.LanguageCode](./languagecode-swift.struct/odia.md)
- [static var pashto: Locale.LanguageCode](./languagecode-swift.struct/pashto.md)
- [static var persian: Locale.LanguageCode](./languagecode-swift.struct/persian.md)
- [static var polish: Locale.LanguageCode](./languagecode-swift.struct/polish.md)
- [static var portuguese: Locale.LanguageCode](./languagecode-swift.struct/portuguese.md)
- [static var punjabi: Locale.LanguageCode](./languagecode-swift.struct/punjabi.md)
- [static var rohingya: Locale.LanguageCode](./languagecode-swift.struct/rohingya.md)
- [static var romanian: Locale.LanguageCode](./languagecode-swift.struct/romanian.md)
- [static var russian: Locale.LanguageCode](./languagecode-swift.struct/russian.md)
- [static var samoan: Locale.LanguageCode](./languagecode-swift.struct/samoan.md)
- [static var sanskrit: Locale.LanguageCode](./languagecode-swift.struct/sanskrit.md)
- [static var santali: Locale.LanguageCode](./languagecode-swift.struct/santali.md)
- [static var serbian: Locale.LanguageCode](./languagecode-swift.struct/serbian.md)
- [static var sindhi: Locale.LanguageCode](./languagecode-swift.struct/sindhi.md)
- [static var sinhala: Locale.LanguageCode](./languagecode-swift.struct/sinhala.md)
- [static var slovak: Locale.LanguageCode](./languagecode-swift.struct/slovak.md)
- [static var slovenian: Locale.LanguageCode](./languagecode-swift.struct/slovenian.md)
- [static var spanish: Locale.LanguageCode](./languagecode-swift.struct/spanish.md)
- [static var swahili: Locale.LanguageCode](./languagecode-swift.struct/swahili.md)
- [static var swedish: Locale.LanguageCode](./languagecode-swift.struct/swedish.md)
- [static var tagalog: Locale.LanguageCode](./languagecode-swift.struct/tagalog.md)
- [static var tajik: Locale.LanguageCode](./languagecode-swift.struct/tajik.md)
- [static var tamil: Locale.LanguageCode](./languagecode-swift.struct/tamil.md)
- [static var telugu: Locale.LanguageCode](./languagecode-swift.struct/telugu.md)
- [static var thai: Locale.LanguageCode](./languagecode-swift.struct/thai.md)
- [static var tibetan: Locale.LanguageCode](./languagecode-swift.struct/tibetan.md)
- [static var tongan: Locale.LanguageCode](./languagecode-swift.struct/tongan.md)
- [static var turkish: Locale.LanguageCode](./languagecode-swift.struct/turkish.md)
- [static var turkmen: Locale.LanguageCode](./languagecode-swift.struct/turkmen.md)
- [static var ukrainian: Locale.LanguageCode](./languagecode-swift.struct/ukrainian.md)
- [static let unavailable: Locale.LanguageCode](./languagecode-swift.struct/unavailable.md)
  The `zxx` code: used in cases when the content is not in any particular languages, such as images, symbols, etc.
- [static let uncoded: Locale.LanguageCode](./languagecode-swift.struct/uncoded.md)
  The `mis` code: represents languages that have not been included in the ISO standard yet
- [static let unidentified: Locale.LanguageCode](./languagecode-swift.struct/unidentified.md)
  The `und` code: used in cases where the language has not been identified
- [static var urdu: Locale.LanguageCode](./languagecode-swift.struct/urdu.md)
- [static var uyghur: Locale.LanguageCode](./languagecode-swift.struct/uyghur.md)
- [static var uzbek: Locale.LanguageCode](./languagecode-swift.struct/uzbek.md)
- [static var vietnamese: Locale.LanguageCode](./languagecode-swift.struct/vietnamese.md)
- [static var welsh: Locale.LanguageCode](./languagecode-swift.struct/welsh.md)
- [static var yiddish: Locale.LanguageCode](./languagecode-swift.struct/yiddish.md)
### Enumerations
- [Locale.LanguageCode.IdentifierType](./languagecode-swift.struct/identifiertype.md)
  Types of ISO 639 language code.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Examining language properties
- [var languageCode: Locale.LanguageCode?](./language-swift.struct/languagecode.md)
  The language code that identifies the language.
- [var region: Locale.Region?](./language-swift.struct/region.md)
  The region used with the language.
- [Locale.Region](./region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var script: Locale.Script?](./language-swift.struct/script.md)
  The written script of the language.
- [Locale.Script](./script.md)
  The written script used with a given language.
- [var characterDirection: Locale.LanguageDirection](./language-swift.struct/characterdirection.md)
  The ordering of characters within a line.
- [typealias LanguageDirection](./languagedirection.md)
  An alias for the standard set of language directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/languagecode-swift.struct)*