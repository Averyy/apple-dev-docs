# status(for:to:)

**Framework**: Translation  
**Kind**: method

Checks to see if a language pairing is supported based off a string of sample text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
func status(for text: String, to target: Locale.Language?) async throws -> LanguageAvailability.Status
```

#### Return Value

The availability status for the language pairing to use in the translation.

#### Discussion

Use this function when you don’t know the source language and you want the framework to attempt a translation for you based on the sample text you pass in.

Pass in a string of sample `text` representing the language you want to translate from. When you do, the system automatically tries to detect the language of the text you pass in. If it can’t, it throws a [`TranslationError`](translationerror.md).

If it can detect the source language of the text, it checks to see if the necessary language assets have downloaded and are ready for use.

> **Note**: For best results in automatic language detection, pass in a sample string of at least 20 characters in length.

## Parameters

- `text`: A sample string of text representing the source language you want to translation from.
- `target`: The target language you want to translate content into. When set to    the system picks an appropriate target based on the user’s preferred languages and returns   the status for those languages.

## See Also

- [func status(from: Locale.Language, to: Locale.Language?) async -> LanguageAvailability.Status](languageavailability/status(from:to:).md)
  Checks to see if a specific language pairing is installed and ready for translation.
- [LanguageAvailability.Status](languageavailability/status.md)
  The availability status for a language or language pairing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/status(for:to:))*