# init(components:)

**Framework**: Foundation  
**Kind**: init

Creates a locale from the given components.

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
init(components: Locale.Components)
```

#### Discussion

Use this initializer to create a locale with a unique combination of components, beyond the defaults provided by a language and country code.

For example, you can create a [`Locale.Components`](locale/components.md) instance that uses UK language conventions, but US regional conventions for traits like currency and measurement. You then use the components to create a new [`Locale`](locale.md) instance, like this:

```swift
var components = Locale.Components(languageCode: "en", languageRegion: "GB")
components.region = Locale.Region("US")
let en_GB_US = Locale(components: components)
```

## Parameters

- `components`: A   instance that provides the components to create a customized locale.

## See Also

- [Locale.Components](locale/components.md)
  A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](locale/init(languagecode:script:languageregion:).md)
  Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents: Locale.Language.Components)](locale/init(languagecomponents:).md)
  Creates a locale from the given language components.
- [Locale.Language.Components](locale/language-swift.struct/components.md)
  A type that identifies a language by its various components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/init(components:))*