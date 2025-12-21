# TranslationSession.BatchResponse

**Framework**: Translation  
**Kind**: struct

A type that provides asynchronous access to translation responses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
struct BatchResponse
```

#### Overview

This type returns instances of [`TranslationSession.Response`](translationsession/response.md) asynchronously and throws an `Error` if something goes wrong.

## Topics

### Structures
- [TranslationSession.BatchResponse.AsyncIterator](translationsession/batchresponse/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Instance Methods
- [func makeAsyncIterator() -> TranslationSession.BatchResponse.AsyncIterator](translationsession/batchresponse/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Type Aliases
- [TranslationSession.BatchResponse.Element](translationsession/batchresponse/element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func translate(String) async throws -> TranslationSession.Response](translationsession/translate(_:).md)
  Translates a single string of text.
- [func translate(batch: [TranslationSession.Request]) -> TranslationSession.BatchResponse](translationsession/translate(batch:).md)
  Translates multiple strings of text of the same language, returning a sequence of responses as they’re available.
- [func translations(from: [TranslationSession.Request]) async throws -> [TranslationSession.Response]](translationsession/translations(from:).md)
  Translates multiple strings of text of the same language, returning the results all at once when complete.
- [TranslationSession.Request](translationsession/request.md)
  A translation request containing a single item of text to translate.
- [TranslationSession.Response](translationsession/response.md)
  The response to a translation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/batchresponse)*