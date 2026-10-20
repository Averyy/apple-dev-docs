# Locale.Script

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(String)](./script/init%28_%29.md)
  Creates a script from a BCP 47 identifier.
- [init(stringLiteral: String)](./script/init%28stringliteral%29.md)
  Creates a script from a BCP 47 identifier as a string literal.
### Examining script properties
- [var identifier: String](./script/identifier.md)
### Using defined scripts
- [static let unknown: Locale.Script](./script/unknown.md)
  Represents an uncoded script
### Instance Properties
- [var isISOScript: Bool](./script/isisoscript.md)
  Returns if the script is an ISO 15924 script
### Type Properties
- [static var adlam: Locale.Script](./script/adlam.md)
- [static var arabic: Locale.Script](./script/arabic.md)
- [static var arabicNastaliq: Locale.Script](./script/arabicnastaliq.md)
- [static var armenian: Locale.Script](./script/armenian.md)
- [static var bangla: Locale.Script](./script/bangla.md)
- [static var cherokee: Locale.Script](./script/cherokee.md)
- [static var cyrillic: Locale.Script](./script/cyrillic.md)
- [static var devanagari: Locale.Script](./script/devanagari.md)
- [static var ethiopic: Locale.Script](./script/ethiopic.md)
- [static var georgian: Locale.Script](./script/georgian.md)
- [static var greek: Locale.Script](./script/greek.md)
- [static var gujarati: Locale.Script](./script/gujarati.md)
- [static var gurmukhi: Locale.Script](./script/gurmukhi.md)
- [static var hanSimplified: Locale.Script](./script/hansimplified.md)
- [static var hanTraditional: Locale.Script](./script/hantraditional.md)
- [static var hanifiRohingya: Locale.Script](./script/hanifirohingya.md)
- [static var hebrew: Locale.Script](./script/hebrew.md)
- [static var hiragana: Locale.Script](./script/hiragana.md)
- [static var japanese: Locale.Script](./script/japanese.md)
- [static var kannada: Locale.Script](./script/kannada.md)
- [static var katakana: Locale.Script](./script/katakana.md)
- [static var khmer: Locale.Script](./script/khmer.md)
- [static var korean: Locale.Script](./script/korean.md)
- [static var lao: Locale.Script](./script/lao.md)
- [static var latin: Locale.Script](./script/latin.md)
- [static var malayalam: Locale.Script](./script/malayalam.md)
- [static var meiteiMayek: Locale.Script](./script/meiteimayek.md)
- [static var myanmar: Locale.Script](./script/myanmar.md)
- [static var odia: Locale.Script](./script/odia.md)
- [static var olChiki: Locale.Script](./script/olchiki.md)
- [static var sinhala: Locale.Script](./script/sinhala.md)
- [static var syriac: Locale.Script](./script/syriac.md)
- [static var tamil: Locale.Script](./script/tamil.md)
- [static var telugu: Locale.Script](./script/telugu.md)
- [static var thaana: Locale.Script](./script/thaana.md)
- [static var thai: Locale.Script](./script/thai.md)
- [static var tibetan: Locale.Script](./script/tibetan.md)

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
- [Locale.LanguageCode](./languagecode-swift.struct.md)
  An alphabetical code associated with a language.
- [var region: Locale.Region?](./language-swift.struct/region.md)
  The region used with the language.
- [Locale.Region](./region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var script: Locale.Script?](./language-swift.struct/script.md)
  The written script of the language.
- [var characterDirection: Locale.LanguageDirection](./language-swift.struct/characterdirection.md)
  The ordering of characters within a line.
- [typealias LanguageDirection](./languagedirection.md)
  An alias for the standard set of language directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/script)*