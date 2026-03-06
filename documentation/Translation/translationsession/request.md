# TranslationSession.Request

**Framework**: Translation  
**Kind**: struct

A translation request containing a single item of text to translate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
struct Request
```

#### Overview

Create a translation request to translate a string of text. Initialize the request using [`init(sourceText:clientIdentifier:)`](translationsession/request/init(sourcetext:clientidentifier:)-ruyz.md). Set the [`sourceText`](translationsession/request/sourcetext.md) to the string of text you want to translate. Then pass that request in an array to one of the batch translation functions.

Keep track of the correspondence between the responses and requests by setting the [`clientIdentifier`](translationsession/request/clientidentifier.md) on the sent request, then matching it with the [`clientIdentifier`](translationsession/response/clientidentifier.md) of the received response when the translation completes.

## Topics

### Initializing a translation request
- [init(sourceText: AttributedString, clientIdentifier: String?)](translationsession/request/init(sourcetext:clientidentifier:)-8fung.md)
  Creates a request for translating a single attributed string.
- [init(sourceText: String, clientIdentifier: String?)](translationsession/request/init(sourcetext:clientidentifier:)-ruyz.md)
  Creates a request for translating a single string of text.
### Specifying text to translate
- [var sourceText: String](translationsession/request/sourcetext.md)
  The plain text input to translate.
- [var attributedSourceText: AttributedString?](translationsession/request/attributedsourcetext.md)
  The text to translate, including styling like bold text, italics, and hyperlink data for linking between data sources.
### Identifying requests
- [var clientIdentifier: String?](translationsession/request/clientidentifier.md)
  An optional unique identifier to associate a translation request with its response.

## See Also

- [func translate(AttributedString) async throws -> TranslationSession.Response](translationsession/translate(_:)-59zi2.md)
  Translates a formatted string of text, preserving formatting in the translation.
- [func translate(String) async throws -> TranslationSession.Response](translationsession/translate(_:)-4m20l.md)
  Translates a single string of text.
- [func translate(batch: [TranslationSession.Request]) -> TranslationSession.BatchResponse](translationsession/translate(batch:).md)
  Translates multiple strings of text of the same language, returning a sequence of responses as they’re available.
- [func translations(from: [TranslationSession.Request]) async throws -> [TranslationSession.Response]](translationsession/translations(from:).md)
  Translates multiple strings of text of the same language, returning the results all at once when complete.
- [TranslationSession.Response](translationsession/response.md)
  The response to a translation request.
- [TranslationSession.BatchResponse](translationsession/batchresponse.md)
  A type that provides asynchronous access to translation responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/request)*