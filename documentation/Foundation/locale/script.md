# Locale.Script

**Framework**: Foundation  
**Kind**: struct

The written script used with a given language.

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
struct Script
```

## Topics

### Creating a script
- [init(String)](locale/script/init(_:).md)
  Creates a script from a BCP 47 identifier.
### Examining script properties
- [var identifier: String](locale/script/identifier.md)
### Using defined scripts
- [static let unknown: Locale.Script](locale/script/unknown.md)
  Represents an uncoded script
### Instance Properties
- [var isISOScript: Bool](locale/script/isisoscript.md)
  Returns if the script is an ISO 15924 script
### Type Properties
- [static var adlam: Locale.Script](locale/script/adlam.md)
- [static var arabic: Locale.Script](locale/script/arabic.md)
- [static var arabicNastaliq: Locale.Script](locale/script/arabicnastaliq.md)
- [static var armenian: Locale.Script](locale/script/armenian.md)
- [static var bangla: Locale.Script](locale/script/bangla.md)
- [static var cherokee: Locale.Script](locale/script/cherokee.md)
- [static var cyrillic: Locale.Script](locale/script/cyrillic.md)
- [static var devanagari: Locale.Script](locale/script/devanagari.md)
- [static var ethiopic: Locale.Script](locale/script/ethiopic.md)
- [static var georgian: Locale.Script](locale/script/georgian.md)
- [static var greek: Locale.Script](locale/script/greek.md)
- [static var gujarati: Locale.Script](locale/script/gujarati.md)
- [static var gurmukhi: Locale.Script](locale/script/gurmukhi.md)
- [static var hanSimplified: Locale.Script](locale/script/hansimplified.md)
- [static var hanTraditional: Locale.Script](locale/script/hantraditional.md)
- [static var hanifiRohingya: Locale.Script](locale/script/hanifirohingya.md)
- [static var hebrew: Locale.Script](locale/script/hebrew.md)
- [static var hiragana: Locale.Script](locale/script/hiragana.md)
- [static var japanese: Locale.Script](locale/script/japanese.md)
- [static var kannada: Locale.Script](locale/script/kannada.md)
- [static var katakana: Locale.Script](locale/script/katakana.md)
- [static var khmer: Locale.Script](locale/script/khmer.md)
- [static var korean: Locale.Script](locale/script/korean.md)
- [static var lao: Locale.Script](locale/script/lao.md)
- [static var latin: Locale.Script](locale/script/latin.md)
- [static var malayalam: Locale.Script](locale/script/malayalam.md)
- [static var meiteiMayek: Locale.Script](locale/script/meiteimayek.md)
- [static var myanmar: Locale.Script](locale/script/myanmar.md)
- [static var odia: Locale.Script](locale/script/odia.md)
- [static var olChiki: Locale.Script](locale/script/olchiki.md)
- [static var sinhala: Locale.Script](locale/script/sinhala.md)
- [static var syriac: Locale.Script](locale/script/syriac.md)
- [static var tamil: Locale.Script](locale/script/tamil.md)
- [static var telugu: Locale.Script](locale/script/telugu.md)
- [static var thaana: Locale.Script](locale/script/thaana.md)
- [static var thai: Locale.Script](locale/script/thai.md)
- [static var tibetan: Locale.Script](locale/script/tibetan.md)

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
- [Locale.LanguageCode](locale/languagecode-swift.struct.md)
  An alphabetical code associated with a language.
- [var region: Locale.Region?](locale/language-swift.struct/region.md)
  The region used with the language.
- [Locale.Region](locale/region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var script: Locale.Script?](locale/language-swift.struct/script.md)
  The written script of the language.
- [var characterDirection: Locale.LanguageDirection](locale/language-swift.struct/characterdirection.md)
  The ordering of characters within a line.
- [typealias LanguageDirection](locale/languagedirection.md)
  An alias for the standard set of language directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/script)*