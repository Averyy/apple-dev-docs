# init(source:target:)

**Framework**: Translation  
**Kind**: init  
**Role**: Initializer

Creates a configuration from a source and target language.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
init(source: Locale.Language? = nil, target: Locale.Language? = nil)
```

## Discussion

When creating a translation session configuration it’s best to use `Locale.Language` values that return from [`supportedLanguages`](../../languageavailability/supportedlanguages.md). When you pass other `Locale.Language` values, the framework tries to match to one of these supported languages.

## Parameters

- `source`: The language the source content is in. If `nil` the session tries to identify the language, and prompt the person to pick the source language if it’s unclear. All text translated with this session should be in the same source language.
- `target`: The language to translate content into. If `nil` the session tries to pick a target language according to the person’s [`preferredLanguages`](../../../Foundation/locale/preferredlanguages.md), and the `source`.

## See Also

### Creating a configuration
- [init(source: Locale.Language?, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy)](./init%28source,target,preferredstrategy%29.md)
  Creates a configuration from a source and target language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/init(source:target:))*