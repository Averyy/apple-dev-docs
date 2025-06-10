# Locale.Language.Components

**Framework**: Foundation  
**Kind**: struct

A type that identifies a language by its various components.

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
struct Components
```

## Topics

### Creating a language components instance
- [init(identifier: String)](locale/language-swift.struct/components/init(identifier:).md)
  Creates a language components instance from a language identifier.
- [init(language: Locale.Language)](locale/language-swift.struct/components/init(language:).md)
  Creates a language components instance from an existing language instance.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, region: Locale.Region?)](locale/language-swift.struct/components/init(languagecode:script:region:).md)
  Creates a language components instance from a given language code, script, and region.
### Examining language component properties
- [var languageCode: Locale.LanguageCode?](locale/language-swift.struct/components/languagecode.md)
  The language code that identifies this language.
- [Locale.LanguageCode](locale/languagecode-swift.struct.md)
  An alphabetical code associated with a language.
- [var region: Locale.Region?](locale/language-swift.struct/components/region.md)
  The region used with this language.
- [Locale.Region](locale/region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var script: Locale.Script?](locale/language-swift.struct/components/script.md)
  The written script used by this language.
- [Locale.Script](locale/script.md)
  The written script used with a given language.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(components: Locale.Components)](locale/init(components:).md)
  Creates a locale from the given components.
- [Locale.Components](locale/components.md)
  A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](locale/init(languagecode:script:languageregion:).md)
  Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents: Locale.Language.Components)](locale/init(languagecomponents:).md)
  Creates a locale from the given language components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct/components)*