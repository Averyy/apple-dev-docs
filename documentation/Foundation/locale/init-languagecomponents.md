# init(languageComponents:)

**Framework**: Foundation  
**Kind**: init

Creates a locale from the given language components.

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
init(languageComponents: Locale.Language.Components)
```

## Parameters

- `languageComponents`: A   instance that provides language components that identify a locale.

## See Also

- [init(components: Locale.Components)](locale/init(components:).md)
  Creates a locale from the given components.
- [Locale.Components](locale/components.md)
  A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](locale/init(languagecode:script:languageregion:).md)
  Creates a locale with the specified language code, script, and region identifier.
- [Locale.Language.Components](locale/language-swift.struct/components.md)
  A type that identifies a language by its various components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/init(languagecomponents:))*