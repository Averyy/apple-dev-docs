# Locale.Language

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents a language, as used in a locale.

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
struct Language
```

## Topics

### Creating a language
- [init(identifier: String)](./language-swift.struct/init%28identifier%29.md)
  Creates a language from an identifier.
- [init(components: Locale.Language.Components)](./language-swift.struct/init%28components%29.md)
  Creates a language from its component values.
- [Locale.Language.Components](./language-swift.struct/components.md)
  A type that identifies a language by its various components.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, region: Locale.Region?)](./language-swift.struct/init%28languagecode,script,region%29.md)
  Creates a language from a given language code, script, and region.
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
- [Locale.Script](./script.md)
  The written script used with a given language.
- [var characterDirection: Locale.LanguageDirection](./language-swift.struct/characterdirection.md)
  The ordering of characters within a line.
- [typealias LanguageDirection](./languagedirection.md)
  An alias for the standard set of language directions.
### Examining language relationships
- [var parent: Locale.Language?](./language-swift.struct/parent.md)
  The parent language of this language, if available.
- [func hasCommonParent(with: Locale.Language) -> Bool](./language-swift.struct/hascommonparent%28with%29.md)
  Returns a Boolean value that indicates if the given language shares a common parent with this language.
- [func isEquivalent(to: Locale.Language) -> Bool](./language-swift.struct/isequivalent%28to%29.md)
  Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.
### Using system languages
- [static var systemLanguages: [Locale.Language]](./language-swift.struct/systemlanguages.md)
  An array of the system’s supported languages.
### Instance Properties
- [var lineLayoutDirection: Locale.LanguageDirection](./language-swift.struct/linelayoutdirection.md)
  Ordering of lines within a page. For example, top-to-bottom for English; right-to-left for Mongolian in the Mongolian Script
- [var maximalIdentifier: String](./language-swift.struct/maximalidentifier.md)
  Returns a BCP-47 identifier that always includes the script: “zh-Hant-TW”, “en-Latn-US”
- [var minimalIdentifier: String](./language-swift.struct/minimalidentifier.md)
  Returns a BCP-47 identifier in a minimalist form. Script and region may be omitted. For example, “zh-TW”, “en”

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting language components
- [var language: Locale.Language](./language-swift.property.md)
  The language of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct)*