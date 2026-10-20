# init(components:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a language from its component values.

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
init(components: Locale.Language.Components)
```

## Parameters

- `components`: A [`Locale.Language.Components`](./components.md) instance that provides a custom language code, region, and script for the new [`Locale.Language`](../language-swift.struct.md) instance.

## See Also

### Creating a language
- [init(identifier: String)](./init%28identifier%29.md)
  Creates a language from an identifier.
- [Locale.Language.Components](./components.md)
  A type that identifies a language by its various components.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, region: Locale.Region?)](./init%28languagecode,script,region%29.md)
  Creates a language from a given language code, script, and region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct/init(components:))*