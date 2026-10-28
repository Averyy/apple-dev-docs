# TranslationSession.Response

**Framework**: Translation  
**Kind**: struct  
**Role**: Structure

The response to a translation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
struct Response
```

## Overview

You get a single response structure after you translate a string, or when you call one of the batch translation methods passing in an array of translation requests. When the translation completes, a response instance returns with the translation result along with properties the framework used to perform the translation.

## Topics

### Initializing a response
- [init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceText: String, targetText: String, clientIdentifier: String?)](./response/init%28sourcelanguage,targetlanguage,sourcetext,targettext,clientidentifier%29.md)
  Creates an instance of a translation response.
- [init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceAttributedText: AttributedString, targetAttributedText: AttributedString, clientIdentifier: String?)](./response/init%28sourcelanguage,targetlanguage,sourceattributedtext,targetattributedtext,clientidentifier%29.md)
  Creates an instance of a translation response with formatted text.
### Getting translation results
- [let sourceText: String](./response/sourcetext.md)
  The original text to translate from.
- [let targetText: String](./response/targettext.md)
  The translated text.
- [let attributedSourceText: AttributedString?](./response/attributedsourcetext.md)
  The original translated text, including style formatting and links.
- [let attributedTargetText: AttributedString?](./response/attributedtargettext.md)
  The translated formatted text.
### Getting translation details
- [let sourceLanguage: Locale.Language](./response/sourcelanguage.md)
  The language that the framework translated the text from.
- [let targetLanguage: Locale.Language](./response/targetlanguage.md)
  The language that the framework translated the text into.
- [let clientIdentifier: String?](./response/clientidentifier.md)
  The unique identifier matching the client identifier set in the translation request.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [TranslationSession.BatchResponse](./batchresponse.md)
  A type that provides asynchronous access to translation responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response)*