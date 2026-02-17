# init(source:target:preferredStrategy:)

**Framework**: Translation  
**Kind**: init

Creates a configuration from a source and target language.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.0+
- macOS 26.4+ (Beta)

## Declaration

```swift
init(source: Locale.Language? = nil, target: Locale.Language? = nil, preferredStrategy: TranslationSession.Strategy)
```

#### Discussion

When creating a translation session configuration it’s best to use `Locale.Language` values that return from [`supportedLanguages`](languageavailability/supportedlanguages.md). When you pass other `Locale.Language` values, the framework tries to match to one of these supported languages.

## Parameters

- `source`: The language the source content is in. If   the session tries   to identify the language, and prompt the person to pick the source language if it’s   unclear. All text translated with this session should be in the same source language.
- `target`: The language to translate content into. If   the session tries to   pick a target language according to the person’s  ,   and the  .
- `preferredStrategy`: Specify the preferred translation strategy to use. If   is specified,   the framework can still fall back to the   strategy in some cases, such as when   Apple Intelligence isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/init(source:target:preferredstrategy:))*