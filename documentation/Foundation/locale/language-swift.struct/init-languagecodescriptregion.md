# init(languageCode:script:region:)

**Framework**: Foundation  
**Kind**: init

Creates a language from a given language code, script, and region.

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
init(languageCode: Locale.LanguageCode? = nil, script: Locale.Script? = nil, region: Locale.Region? = nil)
```

## Parameters

- `languageCode`: A language code, typically created from a two- or three-letter language code specified by ISO 639.
- `script`: The script to use for the new locale components instance.
- `region`: The region to use for the new components instance.

## See Also

- [init(identifier: String)](locale/language-swift.struct/init(identifier:).md)
  Creates a language from an identifier.
- [init(components: Locale.Language.Components)](locale/language-swift.struct/init(components:).md)
  Creates a language from its component values.
- [Locale.Language.Components](locale/language-swift.struct/components.md)
  A type that identifies a language by its various components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct/init(languagecode:script:region:))*