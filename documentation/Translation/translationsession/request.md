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

Create a translation request to translate a string of text. Initialize the request using [`init(sourceText:clientIdentifier:)`](translationsession/request/init(sourcetext:clientidentifier:).md). Set the `sourceText` to the string of text you want to translate. Then pass that request in an array to one of the batch translation functions.

Keep track of the correspondence between the responses and requests by setting the [`clientIdentifier`](translationsession/request/clientidentifier.md) on the sent request, then matching it with the [`clientIdentifier`](translationsession/response/clientidentifier.md) of the recieved response when the translation completes.

## Topics

### Initializers
- [init(sourceText: String, clientIdentifier: String?)](translationsession/request/init(sourcetext:clientidentifier:).md)
  Creates a request for translating a single string of text.
### Instance Properties
- [var clientIdentifier: String?](translationsession/request/clientidentifier.md)
  An optional unique identifier to associate a translation request with its response.
- [var sourceText: String](translationsession/request/sourcetext.md)
  The input text the framework translates.

## See Also

- [func translate(String) async throws -> TranslationSession.Response](translationsession/translate(_:).md)
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