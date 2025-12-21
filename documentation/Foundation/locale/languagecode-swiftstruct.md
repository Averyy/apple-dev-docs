# Locale.LanguageCode

**Framework**: Foundation  
**Kind**: struct

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
- [init(String)](locale/languagecode-swift.struct/init(_:).md)
  Creates a language code from an identifier.
### Examining language code properties
- [var identifier: String](locale/languagecode-swift.struct/identifier.md)
  The identifier used to create the language code.
- [var isISOLanguage: Bool](locale/languagecode-swift.struct/isisolanguage.md)
  A Boolean value that indicates whether this language code is in the list of ISO-defined languages.
### Using ISO-defined language codes
- [static var isoLanguageCodes: [Locale.LanguageCode]](locale/languagecode-swift.struct/isolanguagecodes.md)
  Returns an array of ISO-defined language codes.
### Instance Methods
- [func identifier(Locale.LanguageCode.IdentifierType) -> String?](locale/languagecode-swift.struct/identifier(_:).md)
  Returns the ISO code of the given identifier type. Returns nil if the language isn’t a valid ISO language, or if the specified identifier type isn’t available to the language.
### Type Properties
- [static var ainu: Locale.LanguageCode](locale/languagecode-swift.struct/ainu.md)
- [static var albanian: Locale.LanguageCode](locale/languagecode-swift.struct/albanian.md)
- [static var amharic: Locale.LanguageCode](locale/languagecode-swift.struct/amharic.md)
- [static var apacheWestern: Locale.LanguageCode](locale/languagecode-swift.struct/apachewestern.md)
- [static var arabic: Locale.LanguageCode](locale/languagecode-swift.struct/arabic.md)
- [static var armenian: Locale.LanguageCode](locale/languagecode-swift.struct/armenian.md)
- [static var assamese: Locale.LanguageCode](locale/languagecode-swift.struct/assamese.md)
- [static var assyrian: Locale.LanguageCode](locale/languagecode-swift.struct/assyrian.md)
- [static var azerbaijani: Locale.LanguageCode](locale/languagecode-swift.struct/azerbaijani.md)
- [static var bangla: Locale.LanguageCode](locale/languagecode-swift.struct/bangla.md)
- [static var belarusian: Locale.LanguageCode](locale/languagecode-swift.struct/belarusian.md)
- [static var bodo: Locale.LanguageCode](locale/languagecode-swift.struct/bodo.md)
- [static var bulgarian: Locale.LanguageCode](locale/languagecode-swift.struct/bulgarian.md)
- [static var burmese: Locale.LanguageCode](locale/languagecode-swift.struct/burmese.md)
- [static var cantonese: Locale.LanguageCode](locale/languagecode-swift.struct/cantonese.md)
- [static var catalan: Locale.LanguageCode](locale/languagecode-swift.struct/catalan.md)
- [static var cherokee: Locale.LanguageCode](locale/languagecode-swift.struct/cherokee.md)
- [static var chinese: Locale.LanguageCode](locale/languagecode-swift.struct/chinese.md)
- [static var croatian: Locale.LanguageCode](locale/languagecode-swift.struct/croatian.md)
- [static var czech: Locale.LanguageCode](locale/languagecode-swift.struct/czech.md)
- [static var danish: Locale.LanguageCode](locale/languagecode-swift.struct/danish.md)
- [static var dhivehi: Locale.LanguageCode](locale/languagecode-swift.struct/dhivehi.md)
- [static var dogri: Locale.LanguageCode](locale/languagecode-swift.struct/dogri.md)
- [static var dutch: Locale.LanguageCode](locale/languagecode-swift.struct/dutch.md)
- [static var dzongkha: Locale.LanguageCode](locale/languagecode-swift.struct/dzongkha.md)
- [static var english: Locale.LanguageCode](locale/languagecode-swift.struct/english.md)
- [static var estonian: Locale.LanguageCode](locale/languagecode-swift.struct/estonian.md)
- [static var faroese: Locale.LanguageCode](locale/languagecode-swift.struct/faroese.md)
- [static var finnish: Locale.LanguageCode](locale/languagecode-swift.struct/finnish.md)
- [static var french: Locale.LanguageCode](locale/languagecode-swift.struct/french.md)
- [static var fula: Locale.LanguageCode](locale/languagecode-swift.struct/fula.md)
- [static var georgian: Locale.LanguageCode](locale/languagecode-swift.struct/georgian.md)
- [static var german: Locale.LanguageCode](locale/languagecode-swift.struct/german.md)
- [static var greek: Locale.LanguageCode](locale/languagecode-swift.struct/greek.md)
- [static var gujarati: Locale.LanguageCode](locale/languagecode-swift.struct/gujarati.md)
- [static var hawaiian: Locale.LanguageCode](locale/languagecode-swift.struct/hawaiian.md)
- [static var hebrew: Locale.LanguageCode](locale/languagecode-swift.struct/hebrew.md)
- [static var hindi: Locale.LanguageCode](locale/languagecode-swift.struct/hindi.md)
- [static var hungarian: Locale.LanguageCode](locale/languagecode-swift.struct/hungarian.md)
- [static var icelandic: Locale.LanguageCode](locale/languagecode-swift.struct/icelandic.md)
- [static var igbo: Locale.LanguageCode](locale/languagecode-swift.struct/igbo.md)
- [static var indonesian: Locale.LanguageCode](locale/languagecode-swift.struct/indonesian.md)
- [static var irish: Locale.LanguageCode](locale/languagecode-swift.struct/irish.md)
- [static var italian: Locale.LanguageCode](locale/languagecode-swift.struct/italian.md)
- [static var japanese: Locale.LanguageCode](locale/languagecode-swift.struct/japanese.md)
- [static var kannada: Locale.LanguageCode](locale/languagecode-swift.struct/kannada.md)
- [static var kashmiri: Locale.LanguageCode](locale/languagecode-swift.struct/kashmiri.md)
- [static var kazakh: Locale.LanguageCode](locale/languagecode-swift.struct/kazakh.md)
- [static var khmer: Locale.LanguageCode](locale/languagecode-swift.struct/khmer.md)
- [static var konkani: Locale.LanguageCode](locale/languagecode-swift.struct/konkani.md)
- [static var korean: Locale.LanguageCode](locale/languagecode-swift.struct/korean.md)
- [static var kurdish: Locale.LanguageCode](locale/languagecode-swift.struct/kurdish.md)
- [static var kurdishSorani: Locale.LanguageCode](locale/languagecode-swift.struct/kurdishsorani.md)
- [static var kyrgyz: Locale.LanguageCode](locale/languagecode-swift.struct/kyrgyz.md)
- [static var lao: Locale.LanguageCode](locale/languagecode-swift.struct/lao.md)
- [static var latvian: Locale.LanguageCode](locale/languagecode-swift.struct/latvian.md)
- [static var lithuanian: Locale.LanguageCode](locale/languagecode-swift.struct/lithuanian.md)
- [static var māori: Locale.LanguageCode](locale/languagecode-swift.struct/m_ori.md)
- [static var macedonian: Locale.LanguageCode](locale/languagecode-swift.struct/macedonian.md)
- [static var maithili: Locale.LanguageCode](locale/languagecode-swift.struct/maithili.md)
- [static var malay: Locale.LanguageCode](locale/languagecode-swift.struct/malay.md)
- [static var malayalam: Locale.LanguageCode](locale/languagecode-swift.struct/malayalam.md)
- [static var maltese: Locale.LanguageCode](locale/languagecode-swift.struct/maltese.md)
- [static var manipuri: Locale.LanguageCode](locale/languagecode-swift.struct/manipuri.md)
- [static var marathi: Locale.LanguageCode](locale/languagecode-swift.struct/marathi.md)
- [static var mongolian: Locale.LanguageCode](locale/languagecode-swift.struct/mongolian.md)
- [static let multiple: Locale.LanguageCode](locale/languagecode-swift.struct/multiple.md)
  The `mul` code: represents the language of some content when there are more than one languages
- [static var navajo: Locale.LanguageCode](locale/languagecode-swift.struct/navajo.md)
- [static var nepali: Locale.LanguageCode](locale/languagecode-swift.struct/nepali.md)
- [static var norwegian: Locale.LanguageCode](locale/languagecode-swift.struct/norwegian.md)
- [static var norwegianBokmål: Locale.LanguageCode](locale/languagecode-swift.struct/norwegianbokm_l.md)
- [static var norwegianNynorsk: Locale.LanguageCode](locale/languagecode-swift.struct/norwegiannynorsk.md)
- [static var odia: Locale.LanguageCode](locale/languagecode-swift.struct/odia.md)
- [static var pashto: Locale.LanguageCode](locale/languagecode-swift.struct/pashto.md)
- [static var persian: Locale.LanguageCode](locale/languagecode-swift.struct/persian.md)
- [static var polish: Locale.LanguageCode](locale/languagecode-swift.struct/polish.md)
- [static var portuguese: Locale.LanguageCode](locale/languagecode-swift.struct/portuguese.md)
- [static var punjabi: Locale.LanguageCode](locale/languagecode-swift.struct/punjabi.md)
- [static var rohingya: Locale.LanguageCode](locale/languagecode-swift.struct/rohingya.md)
- [static var romanian: Locale.LanguageCode](locale/languagecode-swift.struct/romanian.md)
- [static var russian: Locale.LanguageCode](locale/languagecode-swift.struct/russian.md)
- [static var samoan: Locale.LanguageCode](locale/languagecode-swift.struct/samoan.md)
- [static var sanskrit: Locale.LanguageCode](locale/languagecode-swift.struct/sanskrit.md)
- [static var santali: Locale.LanguageCode](locale/languagecode-swift.struct/santali.md)
- [static var serbian: Locale.LanguageCode](locale/languagecode-swift.struct/serbian.md)
- [static var sindhi: Locale.LanguageCode](locale/languagecode-swift.struct/sindhi.md)
- [static var sinhala: Locale.LanguageCode](locale/languagecode-swift.struct/sinhala.md)
- [static var slovak: Locale.LanguageCode](locale/languagecode-swift.struct/slovak.md)
- [static var slovenian: Locale.LanguageCode](locale/languagecode-swift.struct/slovenian.md)
- [static var spanish: Locale.LanguageCode](locale/languagecode-swift.struct/spanish.md)
- [static var swahili: Locale.LanguageCode](locale/languagecode-swift.struct/swahili.md)
- [static var swedish: Locale.LanguageCode](locale/languagecode-swift.struct/swedish.md)
- [static var tagalog: Locale.LanguageCode](locale/languagecode-swift.struct/tagalog.md)
- [static var tajik: Locale.LanguageCode](locale/languagecode-swift.struct/tajik.md)
- [static var tamil: Locale.LanguageCode](locale/languagecode-swift.struct/tamil.md)
- [static var telugu: Locale.LanguageCode](locale/languagecode-swift.struct/telugu.md)
- [static var thai: Locale.LanguageCode](locale/languagecode-swift.struct/thai.md)
- [static var tibetan: Locale.LanguageCode](locale/languagecode-swift.struct/tibetan.md)
- [static var tongan: Locale.LanguageCode](locale/languagecode-swift.struct/tongan.md)
- [static var turkish: Locale.LanguageCode](locale/languagecode-swift.struct/turkish.md)
- [static var turkmen: Locale.LanguageCode](locale/languagecode-swift.struct/turkmen.md)
- [static var ukrainian: Locale.LanguageCode](locale/languagecode-swift.struct/ukrainian.md)
- [static let unavailable: Locale.LanguageCode](locale/languagecode-swift.struct/unavailable.md)
  The `zxx` code: used in cases when the content is not in any particular languages, such as images, symbols, etc.
- [static let uncoded: Locale.LanguageCode](locale/languagecode-swift.struct/uncoded.md)
  The `mis` code: represents languages that have not been included in the ISO standard yet
- [static let unidentified: Locale.LanguageCode](locale/languagecode-swift.struct/unidentified.md)
  The `und` code: used in cases where the language has not been identified
- [static var urdu: Locale.LanguageCode](locale/languagecode-swift.struct/urdu.md)
- [static var uyghur: Locale.LanguageCode](locale/languagecode-swift.struct/uyghur.md)
- [static var uzbek: Locale.LanguageCode](locale/languagecode-swift.struct/uzbek.md)
- [static var vietnamese: Locale.LanguageCode](locale/languagecode-swift.struct/vietnamese.md)
- [static var welsh: Locale.LanguageCode](locale/languagecode-swift.struct/welsh.md)
- [static var yiddish: Locale.LanguageCode](locale/languagecode-swift.struct/yiddish.md)
### Enumerations
- [Locale.LanguageCode.IdentifierType](locale/languagecode-swift.struct/identifiertype.md)
  Types of ISO 639 language code.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var languageCode: Locale.LanguageCode?](locale/language-swift.struct/languagecode.md)
  The language code that identifies the language.
- [var region: Locale.Region?](locale/language-swift.struct/region.md)
  The region used with the language.
- [Locale.Region](locale/region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var script: Locale.Script?](locale/language-swift.struct/script.md)
  The written script of the language.
- [Locale.Script](locale/script.md)
  The written script used with a given language.
- [var characterDirection: Locale.LanguageDirection](locale/language-swift.struct/characterdirection.md)
  The ordering of characters within a line.
- [typealias LanguageDirection](locale/languagedirection.md)
  An alias for the standard set of language directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/languagecode-swift.struct)*