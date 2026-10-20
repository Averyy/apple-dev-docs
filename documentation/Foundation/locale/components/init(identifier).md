# init(identifier:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a locale components instance with the specified identifier.

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
init(identifier: String)
```

## Parameters

- `identifier`: A BCP-47 language identifier such as `en-u-nu-thai-ca-buddhist` or an ICU-style identifier such as `en@calendar=buddhist;numbers=thai`.

## See Also

### Creating a locale components instance
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](./init%28languagecode,script,languageregion%29.md)
  Creates a locale components instance with the specified language code, script, and region identifier.
- [init(locale: Locale)](./init%28locale%29.md)
  Creates a language components instance from an existing locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components/init(identifier:))*