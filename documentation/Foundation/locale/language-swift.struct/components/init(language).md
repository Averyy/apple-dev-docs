# init(language:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a language components instance from an existing language instance.

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
init(language: Locale.Language)
```

## Parameters

- `language`: A [`Locale.Language`](../../language-swift.struct.md) instance. This initializer copies over the language code, script, and region from the provided language.

## See Also

### Creating a language components instance
- [init(identifier: String)](./init%28identifier%29.md)
  Creates a language components instance from a language identifier.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, region: Locale.Region?)](./init%28languagecode,script,region%29.md)
  Creates a language components instance from a given language code, script, and region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct/components/init(language:))*