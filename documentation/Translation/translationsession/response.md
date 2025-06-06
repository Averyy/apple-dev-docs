# TranslationSession.Response

**Framework**: Translation  
**Kind**: struct

The response to a translation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
struct Response
```

#### Overview

You get a single response structure after you translate a string, or when you call one of the batch translation methods passing in an array of translation requests. When the translation completes, a response instance returns with the translation result along with properties the framework used to perform the translation.

## Topics

### Initializers
- [init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceText: String, targetText: String, clientIdentifier: String?)](translationsession/response/init(sourcelanguage:targetlanguage:sourcetext:targettext:clientidentifier:).md)
  Creates an instance of a translation response.
### Instance Properties
- [let clientIdentifier: String?](translationsession/response/clientidentifier.md)
  The unique identifier matching the client identifier set in the translation request.
- [let sourceLanguage: Locale.Language](translationsession/response/sourcelanguage.md)
  The language that the framework translated the text from.
- [let sourceText: String](translationsession/response/sourcetext.md)
  The original text to translate from.
- [let targetLanguage: Locale.Language](translationsession/response/targetlanguage.md)
  The language that the framework translated the text into.
- [let targetText: String](translationsession/response/targettext.md)
  The result of the translation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func translate(String) async throws -> TranslationSession.Response](translationsession/translate(_:).md)
  Translates a single string of text.
- [func translate(batch: [TranslationSession.Request]) -> TranslationSession.BatchResponse](translationsession/translate(batch:).md)
  Translates multiple strings of text of the same language, returning a sequence of responses as they’re available.
- [func translations(from: [TranslationSession.Request]) async throws -> [TranslationSession.Response]](translationsession/translations(from:).md)
  Translates multiple strings of text of the same language, returning the results all at once when complete.
- [TranslationSession.Request](translationsession/request.md)
  A translation request containing a single item of text to translate.
- [TranslationSession.BatchResponse](translationsession/batchresponse.md)
  A type that provides asynchronous access to translation responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response)*