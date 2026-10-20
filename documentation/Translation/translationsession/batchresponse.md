# TranslationSession.BatchResponse

**Framework**: Translation  
**Kind**: struct  
**Role**: Structure

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

This type returns instances of [`TranslationSession.Response`](./response.md) asynchronously and throws an `Error` if something goes wrong.

## Topics

### Iterating over translation results
- [func makeAsyncIterator() -> TranslationSession.BatchResponse.AsyncIterator](./batchresponse/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Iteration types
- [TranslationSession.BatchResponse.AsyncIterator](./batchresponse/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [TranslationSession.BatchResponse.Element](./batchresponse/element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Translating the text
- [func translate(AttributedString) async throws -> TranslationSession.Response](./translate%28_%29-59zi2.md)
  Translates a formatted string of text, preserving formatting in the translation.
- [func translate(String) async throws -> TranslationSession.Response](./translate%28_%29-4m20l.md)
  Translates a single string of text.
- [func translate(batch: [TranslationSession.Request]) -> TranslationSession.BatchResponse](./translate%28batch%29.md)
  Translates multiple strings of text of the same language, returning a sequence of responses as they’re available.
- [func translations(from: [TranslationSession.Request]) async throws -> [TranslationSession.Response]](./translations%28from%29.md)
  Translates multiple strings of text of the same language, returning the results all at once when complete.
- [TranslationSession.Request](./request.md)
  A translation request containing a single item of text to translate.
- [TranslationSession.Response](./response.md)
  The response to a translation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/batchresponse)*