# init(source:target:preferredStrategy:)

**Framework**: Translation  
**Kind**: init  
**Role**: Initializer

Creates a configuration from a source and target language.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.0+
- macOS 26.4+

## Declaration

```swift
init(source: Locale.Language? = nil, target: Locale.Language? = nil, preferredStrategy: TranslationSession.Strategy)
```

## Discussion

When creating a translation session configuration it’s best to use `Locale.Language` values that return from [`supportedLanguages`](../../languageavailability/supportedlanguages.md). When you pass other `Locale.Language` values, the framework tries to match to one of these supported languages.

## Parameters

- `source`: The language the source content is in. If `nil` the session tries to identify the language, and prompt the person to pick the source language if it’s unclear. All text translated with this session should be in the same source language.
- `target`: The language to translate content into. If `nil` the session tries to pick a target language according to the person’s [`preferredLanguages`](../../../Foundation/locale/preferredlanguages.md), and the `source`.
- `preferredStrategy`: The translation approach to use. [`highFidelity`](../strategy/highfidelity.md) uses Apple Intelligence models when available, or falls back to [`lowLatency`](../strategy/lowlatency.md) when those models aren’t available. The `lowLatency` strategy uses traditional models and works on all devices.

## See Also

### Creating a configuration
- [init(source: Locale.Language?, target: Locale.Language?)](./init%28source,target%29.md)
  Creates a configuration from a source and target language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/init(source:target:preferredstrategy:))*