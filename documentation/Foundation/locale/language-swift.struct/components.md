# Locale.Language.Components

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(identifier: String)](./components/init%28identifier%29.md)
  Creates a language components instance from a language identifier.
- [init(language: Locale.Language)](./components/init%28language%29.md)
  Creates a language components instance from an existing language instance.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, region: Locale.Region?)](./components/init%28languagecode,script,region%29.md)
  Creates a language components instance from a given language code, script, and region.
### Examining language component properties
- [var languageCode: Locale.LanguageCode?](./components/languagecode.md)
  The language code that identifies this language.
- [Locale.LanguageCode](../languagecode-swift.struct.md)
  An alphabetical code associated with a language.
- [var region: Locale.Region?](./components/region.md)
  The region used with this language.
- [Locale.Region](../region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var script: Locale.Script?](./components/script.md)
  The written script used by this language.
- [Locale.Script](../script.md)
  The written script used with a given language.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating a locale by components
- [init(components: Locale.Components)](../init%28components%29.md)
  Creates a locale from the given components.
- [Locale.Components](../components.md)
  A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](../init%28languagecode,script,languageregion%29.md)
  Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents: Locale.Language.Components)](../init%28languagecomponents%29.md)
  Creates a locale from the given language components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct/components)*