# Locale.Language

**Framework**: Foundation  
**Kind**: struct

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
- [init(identifier: String)](locale/language-swift.struct/init(identifier:).md)
  Creates a language from an identifier.
- [init(components: Locale.Language.Components)](locale/language-swift.struct/init(components:).md)
  Creates a language from its component values.
- [Locale.Language.Components](locale/language-swift.struct/components.md)
  A type that identifies a language by its various components.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, region: Locale.Region?)](locale/language-swift.struct/init(languagecode:script:region:).md)
  Creates a language from a given language code, script, and region.
### Examining language properties
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
- [Locale.Script](locale/script.md)
  The written script used with a given language.
- [var characterDirection: Locale.LanguageDirection](locale/language-swift.struct/characterdirection.md)
  The ordering of characters within a line.
- [typealias LanguageDirection](locale/languagedirection.md)
  An alias for the standard set of language directions.
### Examining language relationships
- [var parent: Locale.Language?](locale/language-swift.struct/parent.md)
  The parent language of this language, if available.
- [func hasCommonParent(with: Locale.Language) -> Bool](locale/language-swift.struct/hascommonparent(with:).md)
  Returns a Boolean value that indicates if the given language shares a common parent with this language.
- [func isEquivalent(to: Locale.Language) -> Bool](locale/language-swift.struct/isequivalent(to:).md)
  Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.
### Using system languages
- [static var systemLanguages: [Locale.Language]](locale/language-swift.struct/systemlanguages.md)
  An array of the system’s supported languages.
### Instance Properties
- [var lineLayoutDirection: Locale.LanguageDirection](locale/language-swift.struct/linelayoutdirection.md)
- [var maximalIdentifier: String](locale/language-swift.struct/maximalidentifier.md)
- [var minimalIdentifier: String](locale/language-swift.struct/minimalidentifier.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var language: Locale.Language](locale/language-swift.property.md)
  The language of a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct)*