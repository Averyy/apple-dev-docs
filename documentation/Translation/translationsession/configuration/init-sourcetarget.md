# init(source:target:)

**Framework**: Translation  
**Kind**: init

Creates a configuration from a source and target language.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
init(source: Locale.Language? = nil, target: Locale.Language? = nil)
```

#### Discussion

When creating a translation session configuration it’s best to use `Locale.Language` values that return from [`supportedLanguages`](languageavailability/supportedlanguages.md). When you pass other `Locale.Language` values the framework tries to match to one of these supported languages.

## Parameters

- `source`: The language the source content is in. If   the session tries   to identify the language, and prompt the user to pick the source language if it’s   unclear. All text translated with this session should be in the same source language.
- `target`: The language to translate content into. If   the session tries to   pick a target language according to the user’s  ,   and the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/init(source:target:))*