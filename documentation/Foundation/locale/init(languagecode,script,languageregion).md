# init(languageCode:script:languageRegion:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a locale with the specified language code, script, and region identifier.

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
init(languageCode: Locale.LanguageCode? = nil, script: Locale.Script? = nil, languageRegion: Locale.Region? = nil)
```

## Parameters

- `languageCode`: A language code, typically created from a two- or three-letter language code specified by ISO 639.
- `script`: The script to use for the new locale components instance.
- `languageRegion`: A language region, typically created from a two-letter BCP 47 region subtag like `US`.

## See Also

### Creating a locale by components
- [init(components: Locale.Components)](./init%28components%29.md)
  Creates a locale from the given components.
- [Locale.Components](./components.md)
  A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageComponents: Locale.Language.Components)](./init%28languagecomponents%29.md)
  Creates a locale from the given language components.
- [Locale.Language.Components](./language-swift.struct/components.md)
  A type that identifies a language by its various components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/init(languagecode:script:languageregion:))*